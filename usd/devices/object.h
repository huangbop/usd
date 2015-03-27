#ifndef OBJECT_H
#define OBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

#define NULL 0
#define UxObject_HEAD UxObject ob_base;

#define UxObject_INIT(o, typeobj) (((UxObject *)(o))->ob_type = (typeobj))


	typedef struct _object {
		struct _object *ob_prev;
		struct _object *ob_next;
		int ob_refcnt;
		struct _typeobject *ob_type;
	} UxObject;

	typedef int (*openfunc)(UxObject *o);
	typedef int (*closefunc)(UxObject *o);
	typedef int (*readfunc)(UxObject *o, void *buf, int len);
	typedef int (*writefunc)(UxObject *o, void *buf, int len);
	
	typedef struct _typeobject {
		UxObject_HEAD
		const char *tp_name;
		openfunc tp_open;
		closefunc tp_close;
		readfunc tp_read;
		writefunc tp_write;
	} UxTypeObject;

	int UxObject_Open(UxObject *o);
	int UxObject_Close(UxObject *o);
	int UxObject_Read(UxObject *o, void *buf, int len);
	int UxObject_Write(UxObject *o, void *buf, int len);
	
	
	extern UxTypeObject UxType_Type;
	
#ifdef __cplusplus
}
#endif
#endif /* OBJECT_H */



