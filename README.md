# Terraform Installation and Usage

This repository contains the IoC and code used by DocLoc.

## Prerequisites

Make sure you have the following installed on your system:

- [Terraform](https://www.terraform.io/downloads.html)

## Installing Terraform

1. Download the latest version of Terraform from the official website: [Terraform Downloads](https://www.terraform.io/downloads.html).

### Verify that Terraform has been installed successfully by running the following command:

```
terraform --version
```

## Using Terraform


1. Clone this repository:

```
git clone git@github.com:imnotUrban/DocLoc.git
cd DocLoc
```

2. Initialize the Terraform project:

```
terraform init
```
3. Create a plan to preview the changes Terraform will make to your infrastructure:

```
terraform plan
```

4. Apply the changes to your infrastructure:
```
terraform apply
```
Confirm the action by typing "yes" when prompted.

Terraform will provision the resources defined in your code.

5. To destroy the provisioned resources, you can use the following command:

```
terraform destroy
```

Confirm the action by typing "yes" when prompted.

# License





