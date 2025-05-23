variable "ecs_container_service_role" {
  type    = string
  default = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceRole"
}

variable "ecs_task_execution_role" {
  type    = string
  default = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}