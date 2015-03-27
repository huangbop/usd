
#include "serial.h"

int main(int argc, char *argv[])
{

	UxObject *o = UxSerial_FromIndex(11);
	
	UxObject_Open(o);

	
	UxObject_Close(o);


	return 0;
}
