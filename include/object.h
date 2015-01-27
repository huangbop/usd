#ifndef _OBJECT_H_
#define _OBJECT_H_
#ifdef __cplusplus
extern "C" {
#endif
	

struct usd_object {
	struct usd_object *prev;
	struct usd_object *next;
	char *name;
	struct usd_type *type;
};

	typedef int (*fn_open)();
	typedef int (*fn_close)();
	typedef int (*fn_read)();
	typedef int (*fn_write)();
	

struct usd_type {
	struct usd_object object;
	char *tp_name;

	fn_open *tp_open;
	fn_close *tp_close;
	fn_read *tp_read;
	fn_write *tp_write;
	
};
	
	
	
#ifdef __cplusplus
}
#endif
#endif /* _OBJECT_H_ */
