# Propuesta comercial  
## RedAgro La Rioja — Plataforma Digital de Trazabilidad y Exposición Productiva Provincial  
### Componente de desarrollo de software

**Presentada por:** Metis Studio  
**Equipo:** Matías Santana · Tomás Castiglioni  
**Destinataria:** María Cecilia Aquino / Provincia de La Rioja  
**Fecha:** noviembre 2026  
**Plazo de ejecución:** 9 meses (inicio estimado: enero)  
**Inversión:** USD 3.500 / mes · Total USD 31.500

---

## 1. Entendimiento del proyecto

RedAgro La Rioja es una plataforma provincial con formato de **red social productiva** y **trazabilidad agropecuaria**. Su objetivo es dar visibilidad a productores, transparentar origen y calidad ante compradores (incluyendo mayoristas), y dotar al Ministerio de Producción de herramientas de acreditación, fiscalización y seguimiento.

El proyecto completo articula tecnología + despliegue territorial. **Esta propuesta cotiza exclusivamente el desarrollo e implementación del software** (web y móvil), con entrega de código fuente al Estado al finalizar el Mes 9, tal como requiere el pliego.

El trabajo de campo (visitas, inspecciones, jornadas BPA, logística departamental) queda a cargo de los equipos territoriales / ministerio; la plataforma se diseña para **recibir, validar y operar** esos datos.

---

## 2. Alcance de software (completo, sin recortes)

Se implementa el alcance tecnológico del documento de proyecto:

### Roles
- **Ciudadano / Comprador** — acceso por correo (código/enlace), exploración, comentarios identificados, mensajes privados.  
- **Productor** — inscripción, acreditación ministerial, vitrina digital, fotos/videos, respuesta a clientes.  
- **Ministerio** — bandeja de altas, aprobación/rechazo/observación, moderación, fiscalización.

### Módulos
1. Autenticación y perfiles diferenciados (hectáreas, cultivos, volúmenes, certificaciones, tipos de venta).  
2. Red social: publicaciones, comentarios, mensajería, moderación.  
3. Geolocalización y rutas (API de mapas): pines, accesos, distancias a rutas troncales (RN 38 / RN 79) y centros urbanos.  
4. Trazabilidad y BPA digital: trabajos culturales, insumos, actas de inspección.  
5. Capacitación digital: manuales y videotutoriales.  
6. Panel ministerial: acreditación, historial, filtros por rubro y departamento.  
7. Media optimizada para 3G/4G rural + fichas compartibles (WhatsApp/redes).

### Entrega soberana
- Código fuente completo (backend, frontend, apps móviles, esquemas de BD).  
- Despliegue inicial en infraestructura bajo control del Estado.  
- Credenciales raíz, llaves y dominios oficiales.  
- Documentación técnica y guías de mantenimiento evolutivo.

Detalle ampliado: ver `alcance.md`.

---

## 3. Fuera de alcance de esta cotización

- Despliegue territorial en 18 departamentos.  
- Visitas a fincas, agrimensura e inspecciones oculares.  
- Talleres BPA presenciales y convenios municipales.  
- Mantenimiento post Mes 9 (cotizable aparte).  
- Costos de infraestructura/licencias del Estado (Maps, storage, servidores).

---

## 4. Mejoras que proponemos (sobre el pliego)

Cumplimos el pliego y, además, proponemos soluciones que elevan la operación real en campo y la sostenibilidad para el Estado:

| Mejora | Por qué importa |
|--------|-----------------|
| Núcleo unificado web + móvil (PWA + app) | Menos fragmentación y menor costo evolutivo para la Provincia |
| Modo offline / campo | Útil con señal intermitente en zonas rurales |
| Tablero de indicadores ministeriales | Visibilidad de adopción, altas y cobertura por departamento |
| Asistente IA para fichas productivas | Acelera la carga de perfiles en jornadas de inscripción |
| Alertas de vencimientos / documentación | Apoyo a control de certificaciones y exigencias documentales |
| Audit log de cambios | Quién modificó qué dato y cuándo |
| Búsqueda avanzada reforzada | Departamento + rubro + geo-radio + modalidad de venta |

Priorización de mejoras: de común acuerdo en Mes 1, sin desplazar obligaciones del pliego.

---

## 5. Stack tecnológico propuesto

| Capa | Tecnología (propuesta) |
|------|------------------------|
| Web | Next.js (React) + PWA |
| Móvil | App nativa multiplataforma (React Native / Expo) sobre el mismo backend |
| API / Backend | Node.js (o runtime equivalente) + API REST/JSON |
| Base de datos | PostgreSQL |
| Auth | Roles diferenciados + acceso ciudadano por magic link / OTP email |
| Media | Storage + pipeline de compresión de imágenes/video |
| Mapas | Google Maps Platform (u API equivalente definida con la Provincia) |
| Hosting | Despliegue soberano en infraestructura provincial |
| Repos | Entrega completa de código fuente al cierre |

Stack definitivo se valida en la mesa de arquitectura del Mes 1.

---

## 6. Inteligencia artificial en el desarrollo

Para un software de 9 meses con alta exigencia institucional, Metis Studio desarrolla con los **mejores modelos disponibles** para cada tarea —priorizando Anthropic de última generación y complementando con herramientas especializadas cuando aporten valor:

| Modelo / capacidad | Uso en este proyecto |
|--------------------|----------------------|
| **Claude Opus 5.5** | Arquitectura, lógica compleja, revisiones profundas |
| **Fable 5** | Implementación sostenida en ciclos largos |
| **Claude Sonnet (última gen.)** | Desarrollo diario de módulos e iteración rápida |
| **Claude Haiku / ligeros** | Tareas de volumen: chequeos, borradores, clasificación |
| **Modelos con visión** | Apoyo en fotos de producción y validaciones visuales |
| **Embeddings / búsqueda semántica** | Buscador y descubrimiento de productores más preciso |

**Incluido en la metodología:** arquitectura, implementación, pruebas, detección de edge cases y documentación continua.  
**En el producto:** asistentes IA (p. ej. ayuda a fichas) como mejora propuesta priorizable.

**Gobernanza del código:** la IA acelera el trabajo; **quien audita, decide y responde por lo entregado es el equipo humano de Metis Studio**. Los modelos están al servicio del desarrollo; la responsabilidad técnica permanece por encima del código generado.

---

## 7. Cronograma (resumen)

| Mes | Hito software |
|-----|----------------|
| 1 | Arquitectura, co-diseño, Alfa (auth/roles/perfiles/admin base) |
| 2 | Avance módulos + sandbox + plan marcha blanca |
| 3 | Marcha blanca, ajustes, Beta |
| 4 | Apertura de altas / circuito de acreditación en producción |
| 5 | Geo operativa + estadísticas parciales |
| 6 | Trazabilidad/BPA digital + corte de mitad de proyecto |
| 7 | Performance, filtros territoriales, soporte a expansión |
| 8 | Consolidación de datos + stress tests |
| 9 | Lanzamiento, entrega de código/llaves/hosting, traspaso |

Cronograma detallado: ver `gantt-9-meses.md`.

---

## 8. Propuesta económica

| Concepto | Monto |
|----------|-------|
| Honorarios mensuales de desarrollo | **USD 3.500** |
| Plazo | 9 meses |
| **Total** | **USD 31.500** |

- Facturación mensual (sin pago único).  
- Acta de conformidad mensual sobre entregables de software.  
- Código fuente y soberanía de datos al Mes 9.  
- Mantenimiento posterior: cotización aparte si se requiere.  
- El honorario cubre el **servicio integral**: dedicación del equipo, herramientas y **costo operativo de los modelos de IA** usados de forma continua durante los 9 meses (no se trata de un monto exclusivamente “de bolsillo” del proveedor).

Detalle: ver `presupuesto.md`.

---

## 9. Equipo, prioridad y disponibilidad

**Metis Studio** — Matías Santana y Tomás Castiglioni.

**Prioridad exclusiva:** durante estos 9 meses, RedAgro La Rioja será el **único** desarrollo de CRM / plataforma que tome Metis Studio. Es la máxima prioridad del estudio: no se reparte el equipo entre varios productos en paralelo como suele ocurrir en una software factory.

Compromisos:
- Disponibilidad en **horario laboral** para reuniones con equipos técnicos del organismo.  
- Participación en mesas de co-diseño y marcha blanca.  
- Comunicación directa con la contraparte (WhatsApp / canales acordados).  
- Cumplimiento de hitos de software sujetos a dependencias del organismo (infraestructura, feedback, datos de campo).  
- Auditoría humana de todo el código asistido por IA antes de cada entrega.

---

## 10. Condiciones y riesgos gestionados

- Demoras por dependencia de la Provincia / financiador / equipos territoriales **no se imputan** al proveedor de software.  
- El alcance territorial no forma parte de esta cotización (queda explícito para evitar grises).  
- Año electoral: se prioriza transferencia temprana de conocimiento y documentación para sostenibilidad institucional.  
- Posibles multas por incumplimiento aplican a hitos de software bajo control del equipo; no a operaciones de campo ajenas.

---

## 11. Próximos pasos

1. Revisión de esta propuesta con Cecilia / Provincia.  
2. Ajustes menores de alcance o priorización de mejoras.  
3. Demo clickeable de pantallas clave (perfil productor, mapa, panel ministerio, trazabilidad).  
4. Definición contractual vía la estructura que designe la contraparte (SRL / empresa con trayectoria).  
5. Kickoff técnico en enero.

---

## Anexos

- `alcance.md` — alcance incluido, exclusiones y mejoras  
- `gantt-9-meses.md` — cronograma y entregables mensuales  
- `presupuesto.md` — desglose comercial  
- `demo/` — prototipo clickeable de referencia visual

---

**Metis Studio**  
Propuesta RedAgro La Rioja — Solo software · Noviembre 2026
