#include "serial.h"
#include "stdio.h"
#include "stdlib.h"
#include "windows.h"


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
	char name[32] = {0};
	HANDLE handle;

	sprintf(name, "\\\\.\\COM%d", o->index);

	handle = CreateFile(name, GENERIC_READ | GENERIC_WRITE, 0, NULL,
			    OPEN_EXISTING, FILE_FLAG_OVERLAPPED, NULL);

	if (handle == INVALID_HANDLE_VALUE)
		return -1;
	o->handle = handle;
	return 0;
}

int serial_close(UxObject *oo){
	UxSerialObject *o = (UxSerialObject *)oo;

	if (o->handle && o->handle != INVALID_HANDLE_VALUE) {
		if (CloseHandle(o->handle))
			return 0;
	}
	return -1;
}



UxTypeObject UxSerial_Type = {
	{0, 0, 0, &UxType_Type},
	"serial",
	serial_open,		/* open */
	serial_close,			/* close */
	0,			/* read */
	0,			/* write */
};
