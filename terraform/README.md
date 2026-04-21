# Terraform Exercise - Azure Resource Group Deployment

This exercise will guide you through deploying Azure resources using Terraform.

## Prerequisites

- Azure CLI installed
- Terraform installed
- Azure subscription access

## Step-by-Step Instructions

### 1. Authenticate with Azure

First, log in to your Azure account:

```bash
az login
```

Follow the browser prompt to complete authentication.

### 2. Initialize Terraform

Initialize the Terraform working directory. This downloads the required providers:

```bash
terraform init
```

### 3. Validate Configuration

Check if your Terraform configuration is syntactically valid:

```bash
terraform validate
```

### 4. Plan the Deployment

Create an execution plan to see what Terraform will do:

```bash
terraform plan
```

To save the plan to a file:

```bash
terraform plan -out=tfplan
```

### 5. Apply the Configuration

Deploy the resources to Azure:

```bash
terraform apply
```

Or, if you saved a plan file:

```bash
terraform apply tfplan
```

Type `yes` when prompted to confirm the deployment.

### 6. Verify the Resources

Check that the resources were created in Azure:

```bash
az group list --output table
```

### 7. Clean Up

When you're done, destroy the resources to avoid charges:

```bash
terraform destroy
```

Type `yes` when prompted to confirm the destruction.

## Additional Commands

- **Format your code**: `terraform fmt`
- **Show current state**: `terraform show`
- **List resources in state**: `terraform state list`

## Customization

You can customize the deployment by modifying values in `variables.tf` or by creating a `terraform.tfvars` file:

```hcl
resource_group_name = "my-custom-rg"
location            = "westus"
```

## Troubleshooting

- If authentication fails, try `az account show` to verify you're logged in
- If plan fails, check that your Azure subscription is active
- Use `terraform plan -out=tfplan` to review changes before applying
