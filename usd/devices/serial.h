#ifndef SERIAL_H
#define SERIAL_H
#ifdef __cplusplus
extern "C" {
#endif

#include "object.h"

	typedef struct {
		UxObject_HEAD
		int index;
	} UxSerialObject;
	


	UxObject *UxSerial_FromIndex(int index);





	extern UxTypeObject UxSerial_Type;

#ifdef __cplusplus
}
#endif
#endif /* SERIAL_H */
