# Alcance — RedAgro La Rioja (componente software)

**Proveedor:** Metis Studio  
**Proyecto:** Plataforma Digital de Trazabilidad y Exposición Productiva Provincial (RedAgro La Rioja)  
**Duración:** 9 meses  
**Moneda:** USD

---

## 1. Alcance incluido (software completo según pliego)

Se desarrolla e implementa la plataforma **web y móvil** con el alcance funcional técnico definido en el documento de proyecto, sin recortar módulos.

### 1.1 Estructura de usuarios y roles

| Rol | Capacidades |
|-----|-------------|
| **Ciudadano / Comprador** | Acceso con correo (código o enlace seguro). Recorrer perfiles, ver multimedia, comentar y enviar mensajes privados. Sin perfil público ni publicación de contenido. |
| **Productor / Emprendedor** | Inscripción con datos comerciales, ubicación y rubro. Cuenta en espera hasta acreditación ministerial. Una vez aprobado: vitrina digital, fotos, videos, respuesta a clientes. |
| **Equipo del Ministerio (Administradores)** | Alta/baja/observación de productores, moderación, fiscalización y validación de establecimientos. |

### 1.2 Circuito de aprobación de productores

1. **Solicitud** — el productor se registra y carga datos productivos.  
2. **Revisión** — el Ministerio recibe la ficha; puede solicitar corrección por email u observar/rechazar con motivo formal.  
3. **Habilitación** — se activa la página pública y la carga de multimedia.

### 1.3 Interacción y mensajería

- Comentarios abiertos pero identificados (correo validado).  
- Canal directo de consultas (mensaje privado + notificación en panel y email).  
- Moderación: ocultar comentarios y bloquear remitentes (productor y administrador).

### 1.4 Gestión de fotos y videos

- Compresión y adaptación automática de imágenes para redes 3G/4G rurales.  
- Procesamiento de video con calidad adaptable a la conexión.  
- Fichas y publicaciones compartibles (previews para WhatsApp / redes).

### 1.5 Panel de control ministerial

- Bandeja de acreditación (pendientes por fecha y localidad).  
- Historial de quién aprobó/suspendió y en qué fecha.  
- Filtros territoriales por rubro y departamento.

### 1.6 Módulos funcionales

1. **Autenticación y perfiles diferenciados** — productores (fotos, hectáreas, cultivos, volúmenes, certificaciones, modalidades de venta); agentes ministeriales; compradores con buscador geolocalizado (acceso libre sin registro obligatorio para exploración).  
2. **Geolocalización y rutas** — integración API de mapas (Google Maps u equivalente): pines, accesos, distancias y rutas hacia rutas troncales (RN 38, RN 79) y centros urbanos.  
3. **Trazabilidad y BPA** — historial digital de trabajos culturales, insumos aplicados y actas/fichas de inspección de campo (cargables por ministerio / equipos de campo).  
4. **Capacitación digital** — repositorio de manuales, guías y videotutoriales para productores y personal ministerial.  
5. **Documentación técnica** — arquitectura, diagramas de base de datos y guías de mantenimiento evolutivo para el Estado.

### 1.7 Propiedad estatal y entrega

- Código fuente completo (backend, frontend, apps móviles, esquemas de BD) en repositorios oficiales, sin licencias privativas de pago anual.  
- Hosting y despliegue inicial soberano en infraestructura bajo control del Estado provincial.  
- Entrega de credenciales raíz, llaves y administración de dominios oficiales.  
- Entornos: desarrollo, sandbox/marcha blanca y producción.  
- Pruebas de estrés y estabilidad ante carga masiva de productores.

### 1.8 Insumos pedagógicos de software (no territorio)

- Manuales digitales de uso de la plataforma.  
- Videotutoriales cortos (registro, carga de fotos, actualización de volúmenes/tipos de venta).  
- Guías operativas para agentes ministeriales del panel de fiscalización.

---

## 2. Fuera de alcance (territorio y operaciones de campo)

Quedan **excluidos** de esta cotización (corresponden a equipos territoriales / ministerio / otros contratistas):

- Despliegue territorial en los 18 departamentos.  
- Visitas presenciales a fincas, agrimensura e inspecciones oculares.  
- Convenios operativos con municipios y logística de jornadas.  
- Talleres presenciales de Buenas Prácticas Agrícolas (BPA).  
- Impresión física masiva de manuales.  
- Muestreo testigo de campo del ministerio.  
- Rendición contable del proyecto ante el financiador (salvo informes técnicos de software acordados).

**Importante:** la plataforma **sí incluye** los formularios, APIs y paneles necesarios para que ministerio y equipos de campo carguen geolocalización, fichas de inspección y datos de trazabilidad.

---

## 3. Mejoras propuestas (valor diferencial, encima del pliego)

Estas mejoras **no reemplazan** obligaciones del pliego; se ofrecen como soluciones superiores alineadas al mismo objetivo.

| Mejora | Beneficio |
|--------|-----------|
| **Arquitectura unificada web + móvil (PWA + app)** | Un solo núcleo de producto, menor costo de mantenimiento evolutivo para el Estado y experiencia consistente en campo. |
| **Modo offline / campo** | Carga diferida de fotos y fichas con señal intermitente en zonas rurales. |
| **Panel de indicadores ministeriales** | Tablero de adopción por departamento, altas pendientes, perfiles auditados y cobertura geográfica. |
| **Asistente IA para fichas productivas** | Ayuda a redactar y completar descripciones de producción a partir de datos básicos (acelera inscripción). |
| **Alertas de vencimientos / documentación** | Recordatorios de certificaciones o documentación próxima a vencer (compatible con exigencias tipo SENASA a nivel de datos). |
| **Auditoría de cambios (audit log)** | Trazabilidad de quién modificó qué dato productivo y cuándo. |
| **Búsqueda avanzada reforzada** | Filtros combinados por departamento, rubro, modalidad de venta, geo-radio y estado de acreditación. |

---

## 4. Metodología con IA (proceso de desarrollo)

El desarrollo se acelera y se sostiene en calidad durante los 9 meses con los **mejores modelos disponibles** para cada tipo de tarea —en particular la familia Anthropic de última generación—, por ejemplo:

- **Claude Opus 5.5** — arquitectura, lógica compleja, revisión profunda y decisiones de diseño.  
- **Fable 5** — sesiones largas de implementación y continuidad en un proyecto de 9 meses.  
- **Claude Sonnet (última generación)** — desarrollo diario de módulos, iteración rápida y buen equilibrio costo/calidad.  
- **Claude Haiku / modelos ligeros** — tareas de alto volumen (clasificación, borradores, chequeos rutinarios).  
- **Modelos con visión** — apoyo en flujos de fotos de producción, calidad de imagen y validaciones visuales asistidas.  
- **Embeddings / búsqueda semántica** (cuando aporte valor) — buscador de productores y contenidos más preciso.

**Responsabilidad humana:** por más que el desarrollo se apoye en estos modelos, **quien audita, decide y responde por el código es el equipo de Metis Studio**. La IA es una herramienta de aceleración; la supervisión técnica, el criterio de producto y la calidad entregable quedan siempre por encima del modelo.

La IA de **producto** (asistentes en la plataforma) se presenta como mejora propuesta; la IA de **desarrollo** está incluida en la metodología del equipo.

---

## 5. Dependencias del organismo

Para el cumplimiento de hitos de software se requiere del Ministerio / contraparte:

- Disponibilidad para mesas de co-diseño (Mes 1) y feedback de marcha blanca (Meses 2–3).  
- Definición de infraestructura de hosting soberano y dominios.  
- Acceso a equipos técnicos para pruebas.  
- Carga o integración de datos de campo por parte de los responsables territoriales.

Demoras atribuibles a la contraparte no se computan como incumplimiento del proveedor de software.
