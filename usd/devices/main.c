
#include "serial.h"

int main(int argc, char *argv[])
{

	UxObject *o = UxSerial_FromIndex(9);
	
	UxObject_Open(o);

	
	UxObject_Close(o);


	return 0;
}
