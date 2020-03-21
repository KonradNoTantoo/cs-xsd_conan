#pragma once

#include <memory>
#include <vector>

namespace ct
{

enum Dimension : unsigned
{
	_2D = 2,
	_3D = 3
};

class shape
{
public:
	shape() = default;
	virtual ~shape() = default;

private:
	std::string _id;
};

template<Dimension DIM>
class nshape : public shape
{
public:
	nshape() = default;
};

class square : public nshape<_2D>
{
public:
	square() = default;	
};

class circle : public nshape<_2D>
{
public:
	circle() = default;	
};

class cube : public nshape<_2D>
{
public:
	cube() = default;	
};

class sphere : public nshape<_2D>
{
public:
	sphere() = default;	
};

typedef std::vector<std::unique_ptr<shape>> shapes;

}