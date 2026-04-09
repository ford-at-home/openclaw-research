# AWS Setup for GitHub Actions

The index pipeline uses OIDC to assume an IAM role — no static credentials stored in GitHub Secrets.

## Required GitHub Variables

Set these in **Settings → Secrets and variables → Actions → Variables** (not Secrets):

| Variable | Example value |
|---|---|
| `AWS_ROLE_ARN` | `arn:aws:iam::123456789012:role/openclaw-research-deploy` |
| `AWS_REGION` | `us-east-1` |
| `EC2_INSTANCE_ID` | `i-0132ce26b522ba128` |

## IAM Role: `openclaw-research-deploy`

### Trust Policy

Allows only the `main` branch of this repo to assume the role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::ACCOUNT_ID:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com"
        },
        "StringLike": {
          "token.actions.githubusercontent.com:sub": "repo:ford-at-home/openclaw-research:ref:refs/heads/main"
        }
      }
    }
  ]
}
```

### Permission Policy

Minimum permissions needed:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "SSMNotify",
      "Effect": "Allow",
      "Action": [
        "ssm:SendCommand",
        "ssm:GetCommandInvocation"
      ],
      "Resource": [
        "arn:aws:ec2:REGION:ACCOUNT_ID:instance/INSTANCE_ID",
        "arn:aws:ssm:REGION::document/AWS-RunShellScript"
      ]
    }
  ]
}
```

Optional — add these if you want Bedrock vectorization later:

```json
{
  "Sid": "BedrockEmbed",
  "Effect": "Allow",
  "Action": ["bedrock:InvokeModel"],
  "Resource": ["arn:aws:bedrock:REGION::foundation-model/amazon.titan-embed-text-v2:0"]
}
```

## OIDC Provider

If not already created in the account:

```bash
aws iam create-open-id-connect-provider \
  --url https://token.actions.githubusercontent.com \
  --client-id-list sts.amazonaws.com \
  --thumbprint-list 6938fd4d98bab03faadb97b34396831e3780aea1 \
  --profile mvp
```

## Verify

After creating the role and setting the variables, push a test `.md` file to `main`. The Action will:
1. Rebuild `index.json` + `README.md`
2. Commit them back (`[skip ci]` prevents infinite loop)
3. Send an SSM command to the EC2 instance
4. OpenClaw delivers the notification to WhatsApp
