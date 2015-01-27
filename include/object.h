#ifndef _OBJECT_H_
#define _OBJECT_H_
#ifdef __cplusplus
extern "C" {
#endif
	

struct usd_object {
	struct usd_object *prev;
	struct usd_object *next;
	struct usd_type *type;
	char *name;
};

struct usd_type {
	struct usd_object object;
	char *tp_name;

	/* func_open *tp_open; */
	/* func_close *tp_close; */
	/* func_read *tp_read; */
	/* func_write *tp_write; */
	
};
	
	
	
#ifdef __cplusplus
}
#endif
#endif /* _OBJECT_H_ */
