#include "object.h"



int UxObject_Open(UxObject *o)
{
	openfunc of = o->ob_type->tp_open;

	if (of)
		return of(o);
	return -1;
}
	


int UxObject_Close(UxObject *o)
{
	return -1;
}

int UxObject_Read(UxObject *o, void *buf, int len)
{
	return -1;
}

int UxObject_Write(UxObject *o, void *buf, int len)
{
	return -1;
}



















UxTypeObject UxType_Type = {
	{0, 0, 0, &UxType_Type},
	"type",
	0,
	0,
	0,
	0,
};

