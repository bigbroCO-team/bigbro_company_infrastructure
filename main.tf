module "vpc" {
  source       = "./modules/vpc"
  vpc_cidr     = var.vpc_cidr
  project_name = var.project_name
}

module "s3" {
  source       = "./modules/s3"
  project_name = var.project_name
}

module "ecr" {
  source       = "./modules/ecr"
  project_name = var.project_name
}

module "ecs" {
  source                      = "./modules/ecs"
  project_name                = var.project_name
  bigbro_stage_tg_arn         = module.ec2.bigbro_stage_tg_arn
  ecs_task_execution_role_arn = module.iam.ecs_task_execution_role_arn
  ecs_task_role_arn           = module.iam.ecs_task_role_arn
  public_subnet_1_id          = module.vpc.public_subnet_1_id
  public_subnet_2_id          = module.vpc.public_subnet_2_id
  bigbro_vpc_id               = module.vpc.bigbro_vpc_id
  bigbro_alb_sg_id            = module.ec2.bigbro_alb_sg_id
  aws_region                  = var.aws_region
}

module "ec2" {
  source             = "./modules/ec2"
  project_name       = var.project_name
  bigbro_vpc_id      = module.vpc.bigbro_vpc_id
  public_subnet_1_id = module.vpc.public_subnet_1_id
  public_subnet_2_id = module.vpc.public_subnet_2_id
}

module "iam" {
  source = "./modules/iam"
}