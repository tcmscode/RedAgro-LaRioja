# Cronograma / Gantt — RedAgro La Rioja (componente software)

**Duración:** 9 meses  
**Proveedor:** Metis Studio  
**Nota:** Los hitos territoriales del pliego (visitas, convenios municipales, inspecciones físicas) quedan a cargo de equipos de campo / ministerio. Aquí se listan los **entregables de software** alineados a cada mes.

---

## Vista Gantt (meses 1–9)

| Hito / trabajo | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 |
|----------------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Co-diseño y arquitectura | ██ | | | | | | | | |
| Auth, roles, panel ministerio base | ██ | ██ | | | | | | | |
| Perfiles productor + buscador | ██ | ██ | ██ | | | | | | |
| Red social (posts, comentarios, DM) | | ██ | ██ | ██ | | | | | |
| Media (fotos/videos, compresión) | | ██ | ██ | ██ | | | | | |
| Geolocalización y rutas (Maps) | | ██ | ██ | ██ | ██ | | | | |
| Trazabilidad / BPA digital | | | ██ | ██ | ██ | ██ | | | |
| Repositorio de capacitación digital | | | ██ | ██ | | | | | |
| Sandbox + marcha blanca + ajustes | | ██ | ██ | | | | | | |
| Soporte a altas masivas / APIs campo | | | | ██ | ██ | ██ | ██ | ██ | |
| Indicadores / mejoras acordadas | | | | | ██ | ██ | ██ | | |
| Stress test y hardening | | | | | | ██ | ██ | ██ | |
| Entrega código, llaves, hosting | | | | | | | | | ██ |
| Lanzamiento y traspaso técnico | | | | | | | | | ██ |

---

## Entregables mensuales (software)

### Mes 1 — Inicio, arquitectura y co-diseño
**Hito:** Puesta en marcha formal del componente software.

**Entregables:**
- Informe técnico de arquitectura (web + app móvil).  
- Actas / minutas de mesas de co-diseño con Ministerio y secretarías.  
- Versión Alfa inicial: autenticación por roles, esqueleto de perfiles y panel admin.  
- Backlog priorizado del núcleo funcional.

### Mes 2 — Avance de desarrollo y plan piloto
**Hito:** Cierre de primera versión funcional ampliada (Alfa+) y plan de marcha blanca.

**Entregables:**
- Reporte de módulos: perfiles, buscador, geolocalización inicial, registro de insumos (base).  
- Plan técnico de marcha blanca y selección de usuarios piloto / agentes.  
- Entorno sandbox desplegado.

### Mes 3 — Marcha blanca, ajustes y capacitación temprana (digital)
**Hito:** Validación en entorno real y beta lista para despliegue masivo.

**Entregables:**
- Informe de marcha blanca (errores, correcciones, optimización).  
- Material de capacitación digital para agentes ministeriales + registro de sesiones remotas/presenciales de uso de la herramienta (no talleres BPA territoriales).  
- **Versión Beta** lista para apertura de altas.

### Mes 4 — Apertura de inscripciones (soporte de plataforma)
**Hito:** Plataforma habilitada para primeras altas de productores.

**Entregables:**
- Circuito completo de solicitud → revisión → habilitación en producción (o pre-producción acordada).  
- Panel de acreditación operativo.  
- Reporte de primeras planillas/altas cargadas en el sistema.  
- *(Convenios municipales y jornadas BPA: fuera de alcance software.)*

### Mes 5 — Geolocalización integrada y estadísticas
**Hito:** Mapa operativo y primeras fichas geo vinculadas a perfiles.

**Entregables:**
- Módulo de geolocalización/rutas estable (carga de pines por ministerio/campo).  
- Estadísticas parciales de perfiles en plataforma.  
- Formularios digitales de ficha de campo listos para uso por equipos territoriales.

### Mes 6 — Mitad de ejecución y auditoría de datos (sistema)
**Hito:** Corte técnico a 6 meses.

**Entregables:**
- Módulo de trazabilidad/BPA con historial de insumos, trabajos culturales y actas digitales.  
- Herramientas de contraste declaración vs. inspección (carga de auditoría por ministerio).  
- Reporte de uso del panel por agentes capacitados.  
- *(Certificación física en finca: fuera de alcance software.)*

### Mes 7 — Expansión departamental (capacidad de plataforma)
**Hito:** Plataforma preparada para cobertura del interior.

**Entregables:**
- Mejoras de performance y filtros territoriales.  
- Actualización de matriz de accesos/distancias en sistema a medida que se cargan nuevos establecimientos.  
- Reporte de avance de inscripciones en la base.

### Mes 8 — Consolidación y pruebas de carga
**Hito:** Pre-lanzamiento.

**Entregables:**
- Consolidación de base provincial en plataforma.  
- Informe de pruebas de estrés / estabilidad bajo volumen proyectado.  
- Hardening de seguridad y checklist pre-lanzamiento.

### Mes 9 — Cierre, lanzamiento y transferencia
**Hito:** Entrega definitiva del software al Estado.

**Entregables:**
- Informe técnico final del componente software.  
- Documentación de lanzamiento oficial.  
- Acta de traspaso: repositorios, llaves maestras, hosting soberano, superadmin.  
- Manuales de arquitectura, BD y mantenimiento evolutivo.  
- Propuesta opcional de mantenimiento post-contrato (aparte).

---

## Dependencias críticas

| Dependencia | Impacta |
|-------------|---------|
| Mesas de co-diseño Mes 1 | Arquitectura y alfa |
| Feedback marcha blanca Mes 2–3 | Beta |
| Infraestructura / dominio provincial | Despliegues |
| Carga de datos de campo por terceros | Geo y auditoría Mes 4–8 |
| Disponibilidad horaria laboral para reuniones | Todos los meses |

Demoras de contraparte desplazan hitos sin penalizar al proveedor de software.
