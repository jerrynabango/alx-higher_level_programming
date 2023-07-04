#include "Python.h"

/**
 * print_python_string - Function that prints python string
 *
 * @p: Indicates a piointer to pyobject
 *
 * Return: empty string
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
		{
			printf("  type: compact ascii\n");
		}
		else
		{
			printf("  type: compact unicode object\n");
		}
		printf("  length: %zu\n", PyUnicode_GET_LENGTH(p));
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}