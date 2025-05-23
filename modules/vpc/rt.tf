# Public subnet 1 rt
resource "aws_route_table" "public_subnet_1_rt" {
  vpc_id = aws_vpc.bigbro-vpc.id

  tags = {
    Name    = "public_subnet_1_rt"
    Project = var.project_name
  }
}

resource "aws_route_table_association" "route_table_association_1" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_subnet_1_rt.id
}

resource "aws_route" "public_subnet_1_default_route" {
  route_table_id         = aws_route_table.public_subnet_1_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.bigbro-gw.id
}

# Public subnet 2 rt
resource "aws_route_table" "public_subnet_2_rt" {
  vpc_id = aws_vpc.bigbro-vpc.id

  tags = {
    Name    = "public_subnet_2_rt"
    Project = var.project_name
  }
}

resource "aws_route_table_association" "route_table_association_2" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_subnet_2_rt.id
}

resource "aws_route" "public_subnet_2_default_route" {
  route_table_id         = aws_route_table.public_subnet_2_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.bigbro-gw.id
}
