"""
Nombres físicos de tablas en MySQL — base lahornilla_base_normalizada.
"""

# --- Tablas ---
DIM_CATEGORIA       = "inventario_dim_categoria"
DIM_DESTINO         = "inventario_dim_destino"
DIM_PRODUCTO        = "inventario_dim_producto"
DIM_TIPO_MOVIMIENTO = "inventario_tipo_movimiento"
DIM_USUARIO         = "general_dim_usuario"
DIM_EQUIPOS         = "inventario_dim_equipos"
DIM_CELULARES       = "inventario_dim_celulares"
DIM_TABLETS         = "inventario_dim_tablets"
DIM_IMPRESORAS      = "inventario_dim_impresoras"
FACT_MOVIMIENTOS    = "inventario_fact_movimientos"

# --- PKs dimensiones ---
PK_CATEGORIA       = "id"
PK_DESTINO         = "id"
PK_PRODUCTO        = "id"
PK_TIPO_MOVIMIENTO = "id"
PK_USUARIO         = "id"          # UUID varchar(45)
PK_EQUIPOS         = "id"
PK_CELULARES       = "id"
PK_TABLETS         = "id"
PK_IMPRESORAS      = "id"

# --- Hecho ---
PK_FACT          = "id"
FACT_COL_PRODUCTO = "producto_id"
FACT_COL_TIPO     = "tipo_mov_id"
FACT_COL_DESTINO  = "destino_id"
FACT_COL_USUARIO  = "usuario_id"   # varchar(45) UUID

# --- FKs ---
FK_PRODUCTO_CATEGORIA = "categoria_id"

# --- Usuario ---
COL_USUARIO_LOGIN = "usuario"
COL_USUARIO_PASS  = "clave"

# Vista stock
STOCK_VIEW_DEFAULT = "vw_stock_inventario"
