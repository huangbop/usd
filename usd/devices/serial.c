#include "serial.h"
#include "stdlib.h"



UxObject *
UxSerial_FromIndex(int index)
{
	UxSerialObject *v;

	v = (UxSerialObject *)malloc(sizeof(UxSerialObject));
	if (v) {
		UxObject_INIT(v, &UxSerial_Type);
		v->index = index;
	}

	return (UxObject *)v;
}


int serial_open(UxObject *oo)
{
	UxSerialObject *o = (UxSerialObject *)oo;
	
	
	
	return 0;
}





UxTypeObject UxSerial_Type = {
	{0, 0, 0, &UxType_Type},
	"serial",
	serial_open,		/* open */
	0,			/* close */
	0,			/* read */
	0,			/* write */
};
