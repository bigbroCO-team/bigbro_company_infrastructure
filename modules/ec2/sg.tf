resource "aws_security_group" "bigbro-alb-sg" {
  name        = "bigbro-alb-sg"
  description = "bigbro-alb-sg"
  vpc_id      = var.bigbro_vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
