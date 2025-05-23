resource "aws_security_group" "bigbro-task-sg" {
  name        = "bigbro-task-sg"
  description = "bigbro-task-sg"
  vpc_id      = var.bigbro_vpc_id

  ingress {
    description     = "Allow traffic from ALB"
    from_port       = 80
    to_port         = 80
    protocol        = "tcp"
    security_groups = [var.bigbro_alb_sg_id]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name    = "bigbro-task-sg"
    Project = var.project_name
  }
}
