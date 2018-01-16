Code Generators
===============

Write a code generator that takes the input file in Figure 3.4, and generates
output in two languages of your choice. Try to make it easy to add new
languages.

### Idea of figure 3.4:

```
# Add a product
# to the 'on-order' list
M  AddProduct
F  id          int
F  name        char[30]
F  order_code  int
E
```

Would generate a C code:

```c
/* Add a product */
/* to the 'on-order' list */
typedef struct {
    int  id;
    char name[30];
    int  order_code;
} AddProductMsg;
```

And a Pascal code:

```pascal
{ Add a product }
{ to the 'on-order' list }
AddProductMsg = packed record
    id:         LongInt;
    name:       array[0..29] of char;
    order_code: LongInt;
end;
```
