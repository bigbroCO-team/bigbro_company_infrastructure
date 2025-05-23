output "bigbro_stage_tg_arn" {
  value = aws_alb_target_group.bigbro-stage-tg.arn
}

output "bigbro_alb_sg_id" {
  value = aws_security_group.bigbro-alb-sg.id
}