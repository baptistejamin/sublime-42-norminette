// <--- here error on the second `/`
//23456789012345678901234567890 

//  vvvv------ 1 error
int main(void)
{
	return a;
	if (test)
		return a;
}
//         ^---^--- 2 errors on `a`
ededestaic int test(void)
{

}
	static int test(void)
{
	return (0);
}
		   int test(void)
{
	return (0);
}
	static int test(void)
{
	return 0;
}
//         ^^^^--- 1 on error on `test`

int	n(long	a)
{
	double a;

	return (0);
}

#include "test.h" // <--- here here `include`

int	n(void)
{
	return a;					
	if (test)
		return a;				
}
//         ^---^--- 4 errors: 2 on `a`
//			 ^^^-^^^--------- 2 after `;`

int	n(void)
{
	return (a);	
	if (test)
		return (a);	
}
//             ^---^--- 2 errors after `;`
