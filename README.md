# La Hornilla — Sistema Unificado de Inventario y Activos

## El problema

La Hornilla, empresa agrícola chilena, gestionaba dos sistemas completamente separados para el control de sus recursos tecnológicos:

- **LH Toner** — registraba el consumo y stock de tóners e insumos de impresión
- **LH Inventario** — llevaba el control de activos tecnológicos (computadores, celulares, tablets, impresoras)

Ambos funcionaban como aplicaciones independientes en AppSheet. El resultado era información dispersa, flujos de trabajo duplicados y sin visibilidad unificada del estado real de los recursos de la empresa. Cada consulta requería revisar dos sistemas distintos.

---

## La solución

Se desarrolló desde cero un sistema propio que reemplazó ambas aplicaciones y unificó todo en una sola plataforma centralizada, accesible desde cualquier dispositivo y desplegada en la nube.

**El sistema permite:**

- Registrar entradas y salidas de insumos del inventario general
- Consultar el stock disponible de productos en tiempo real
- Gestionar el catálogo de productos por categoría (tóners, tambores, kits de mantenimiento y repuestos)
- Llevar el registro completo de activos tecnológicos: computadores, celulares corporativos, tablets e impresoras
- Conocer el responsable asignado a cada activo en cualquier momento
- Administrar los usuarios del sistema con control de acceso por roles

---

## El impacto

- **Menos herramientas, menos fricción** — dos aplicaciones reemplazadas por una sola plataforma
- **Información centralizada** — stock, activos y movimientos en un mismo lugar
- **Procesos más ágiles** — los equipos operativos acceden a la información que necesitan sin depender de sistemas externos
- **Control real** — la empresa sabe exactamente qué tiene, dónde está y quién lo usa

---

## Contexto técnico

El backend está construido sobre **Python con FastAPI**, con base de datos **MySQL** y desplegado en **Google Cloud Run**. La autenticación es mediante **JWT**. El sistema está en uso activo dentro de la empresa.

> Proyecto desarrollado internamente en La Hornilla como parte del área de Soporte TI y Desarrollo.
