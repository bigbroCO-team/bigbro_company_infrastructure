variable "project_name" {
  type = string
}

variable "bigbro_stage_tg_arn" {
  type = string
}

variable "ecs_task_execution_role_arn" {
  type = string
}

variable "ecs_task_role_arn" {
  type = string
}

variable "public_subnet_1_id" {
  type = string
}

variable "public_subnet_2_id" {
  type = string
}

variable "bigbro_vpc_id" {
  type = string
}

variable "bigbro_alb_sg_id" {
  type = string
}

variable "aws_region" {
  type = string
}