output "bigbro_vpc_id" {
  description = "vpc id"
  value       = aws_vpc.bigbro-vpc.id
}

output "public_subnet_1_id" {
  description = "public subnet 1 id"
  value       = aws_subnet.public_subnet_1.id
}

output "public_subnet_2_id" {
  description = "public subnet 2 id"
  value       = aws_subnet.public_subnet_2.id
}