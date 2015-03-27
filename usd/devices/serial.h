#ifndef SERIAL_H
#define SERIAL_H
#ifdef __cplusplus
extern "C" {
#endif

#include "object.h"
#include "windows.h"

	typedef struct {
		UxObject_HEAD
		int index;
		HANDLE handle;
	} UxSerialObject;
	


	UxObject *UxSerial_FromIndex(int index);





	extern UxTypeObject UxSerial_Type;

#ifdef __cplusplus
}
#endif
#endif /* SERIAL_H */
