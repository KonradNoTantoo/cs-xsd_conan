#include <cstdlib>
#include <sstream>
#include <iostream>

#include "test_package-pskel.hxx"


class shapes_parser : public conan_test::shapes_pskel
{
public:
	ct::shapes post_shapes () { return ct::shapes(); }
};


int main()
{
	try
	{
		shapes_parser shapes_p;
		xml_schema::document doc_p( shapes_p, "shapes" );

		std::stringstream xml_stream( "<shapes></shapes>" );

		shapes_p.pre();
		doc_p.parse( xml_stream, xml_schema::flags::dont_validate );
		shapes_p.pre();
	}
	catch (const xml_schema::exception& e)
	{
		std::cerr << e << std::endl;
		return EXIT_FAILURE;
	}

	return EXIT_SUCCESS;
}