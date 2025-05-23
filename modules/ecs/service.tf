resource "aws_ecs_service" "bigbro-stage" {
  name            = "bigbro-stage"
  cluster         = aws_ecs_cluster.bigbro-cluster.id
  task_definition = aws_ecs_task_definition.nginx.arn
  desired_count   = 1
  depends_on      = [var.bigbro_stage_tg_arn]

  network_configuration {
    subnets          = [var.public_subnet_1_id, var.public_subnet_2_id]
    security_groups  = [aws_security_group.bigbro-task-sg.id]
    assign_public_ip = false
  }

  ordered_placement_strategy {
    type  = "binpack"
    field = "cpu"
  }

  load_balancer {
    target_group_arn = var.bigbro_stage_tg_arn
    container_name   = "nginx-container"
    container_port   = 80
  }

  tags = {
    Name    = "bigbro-stage"
    Project = var.project_name
  }
}