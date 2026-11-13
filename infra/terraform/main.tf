terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.0" }
  }
}
provider "aws" { region = var.aws_region }
resource "aws_s3_bucket" "bronze" { bucket = var.bronze_bucket_name }
resource "aws_s3_bucket" "curated" { bucket = var.curated_bucket_name }
resource "aws_iam_role" "data_engineer" {
  name = "northstar-data-engineer"
  assume_role_policy = jsonencode({
    Version="2012-10-17",
    Statement=[{Effect="Allow", Principal={Service="ec2.amazonaws.com"}, Action="sts:AssumeRole"}]
  })
}
