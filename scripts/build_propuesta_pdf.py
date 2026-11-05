# -*- coding: utf-8 -*-
"""Genera PDF final de propuesta Metis Studio — RedAgro La Rioja."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Propuesta_Metis_Studio_RedAgro_La_Rioja.pdf"

# Fuentes Windows con soporte UTF-8
FONT_REG = "SegoeUI"
FONT_BOLD = "SegoeUI-Bold"
pdfmetrics.registerFont(TTFont(FONT_REG, r"C:\Windows\Fonts\segoeui.ttf"))
pdfmetrics.registerFont(TTFont(FONT_BOLD, r"C:\Windows\Fonts\segoeuib.ttf"))

INK = colors.HexColor("#1a1a1a")
MUTED = colors.HexColor("#555555")
LINE = colors.HexColor("#cccccc")
RULE = colors.HexColor("#222222")
HEADER_BG = colors.HexColor("#f5f5f5")
ACCENT = colors.HexColor("#1f3d2f")


def styles():
    base = getSampleStyleSheet()
    s = {
        "cover_brand": ParagraphStyle(
            "cover_brand",
            fontName=FONT_BOLD,
            fontSize=11,
            textColor=ACCENT,
            alignment=TA_CENTER,
            spaceAfter=8,
            tracking=1,
        ),
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName=FONT_BOLD,
            fontSize=22,
            textColor=INK,
            alignment=TA_CENTER,
            leading=28,
            spaceAfter=10,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub",
            fontName=FONT_REG,
            fontSize=11,
            textColor=MUTED,
            alignment=TA_CENTER,
            leading=16,
            spaceAfter=6,
        ),
        "meta": ParagraphStyle(
            "meta",
            fontName=FONT_REG,
            fontSize=10,
            textColor=INK,
            alignment=TA_CENTER,
            leading=15,
            spaceAfter=3,
        ),
        "h1": ParagraphStyle(
            "h1",
            fontName=FONT_BOLD,
            fontSize=14,
            textColor=INK,
            spaceBefore=16,
            spaceAfter=8,
            leading=18,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName=FONT_BOLD,
            fontSize=11.5,
            textColor=INK,
            spaceBefore=12,
            spaceAfter=6,
            leading=15,
        ),
        "body": ParagraphStyle(
            "body",
            fontName=FONT_REG,
            fontSize=9.5,
            textColor=INK,
            alignment=TA_JUSTIFY,
            leading=13.5,
            spaceAfter=7,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName=FONT_REG,
            fontSize=9.5,
            textColor=INK,
            leftIndent=12,
            leading=13.5,
            spaceAfter=3,
        ),
        "small": ParagraphStyle(
            "small",
            fontName=FONT_REG,
            fontSize=8.5,
            textColor=MUTED,
            leading=11.5,
            spaceAfter=4,
        ),
        "footer": ParagraphStyle(
            "footer",
            fontName=FONT_REG,
            fontSize=8,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
        "cell": ParagraphStyle(
            "cell",
            fontName=FONT_REG,
            fontSize=8.5,
            textColor=INK,
            leading=11.5,
        ),
        "cell_b": ParagraphStyle(
            "cell_b",
            fontName=FONT_BOLD,
            fontSize=8.5,
            textColor=INK,
            leading=11.5,
        ),
        "annex": ParagraphStyle(
            "annex",
            fontName=FONT_BOLD,
            fontSize=16,
            textColor=INK,
            spaceBefore=4,
            spaceAfter=10,
            leading=20,
        ),
    }
    return s


def hr():
    return HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=4, spaceAfter=10)


def thin_hr():
    return HRFlowable(width="100%", thickness=0.4, color=LINE, spaceBefore=6, spaceAfter=8)


def p(text, style):
    return Paragraph(text, style)


def bullets(items, st):
    return [p(f"• {item}", st["bullet"]) for item in items]


def make_table(headers, rows, col_widths):
    data = [[Paragraph(h, ParagraphStyle("th", fontName=FONT_BOLD, fontSize=8.5, textColor=INK, leading=11)) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), ParagraphStyle("td", fontName=FONT_REG, fontSize=8.5, textColor=INK, leading=11.5)) for c in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
                ("GRID", (0, 0), (-1, -1), 0.4, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(2 * cm, 1.4 * cm, A4[0] - 2 * cm, 1.4 * cm)
    canvas.setFont(FONT_REG, 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(2 * cm, 0.9 * cm, "Metis Studio · RedAgro La Rioja · Confidencial")
    canvas.drawRightString(A4[0] - 2 * cm, 0.9 * cm, f"{doc.page}")
    canvas.restoreState()


def build():
    st = styles()
    story = []

    # ——— PORTADA ———
    story.append(Spacer(1, 3.2 * cm))
    story.append(p("METIS STUDIO", st["cover_brand"]))
    story.append(hr())
    story.append(Spacer(1, 0.4 * cm))
    story.append(p("Propuesta comercial", st["cover_sub"]))
    story.append(
        p(
            "RedAgro La Rioja<br/>Plataforma Digital de Trazabilidad<br/>y Exposición Productiva Provincial",
            st["cover_title"],
        )
    )
    story.append(p("Componente de desarrollo de software", st["cover_sub"]))
    story.append(Spacer(1, 0.8 * cm))
    story.append(thin_hr())
    story.append(p("<b>Destinataria:</b> María Cecilia Aquino / Provincia de La Rioja", st["meta"]))
    story.append(p("<b>Equipo:</b> Matías Santana · Tomás Castiglioni", st["meta"]))
    story.append(p("<b>Fecha:</b> noviembre 2026", st["meta"]))
    story.append(p("<b>Plazo:</b> 9 meses · inicio estimado enero", st["meta"]))
    story.append(Spacer(1, 0.35 * cm))
    story.append(p("<b>Inversión:</b> USD 3.500 / mes · Total USD 31.500", st["meta"]))
    story.append(Spacer(1, 0.35 * cm))
    story.append(thin_hr())
    story.append(
        p(
            "Incluye: propuesta comercial · Anexo A Alcance · Anexo B Presupuesto · Anexo C Cronograma",
            st["small"],
        )
    )
    story.append(
        p(
            "Demo interactiva: se envía en el transcurso del día.",
            st["small"],
        )
    )
    story.append(PageBreak())

    # ——— PROPUESTA ———
    story.append(p("Propuesta comercial", st["h1"]))
    story.append(hr())

    story.append(p("1. Entendimiento del proyecto", st["h2"]))
    story.append(
        p(
            "RedAgro La Rioja es una plataforma provincial con formato de <b>red social productiva</b> y "
            "<b>trazabilidad agropecuaria</b>. Su objetivo es dar visibilidad a productores, transparentar origen "
            "y calidad ante compradores (incluyendo mayoristas), y dotar al Ministerio de Producción de herramientas "
            "de acreditación, fiscalización y seguimiento.",
            st["body"],
        )
    )
    story.append(
        p(
            "El proyecto completo articula tecnología y despliegue territorial. <b>Esta propuesta cotiza exclusivamente "
            "el desarrollo e implementación del software</b> (web y móvil), con entrega de código fuente al Estado al "
            "finalizar el Mes 9, tal como requiere el pliego.",
            st["body"],
        )
    )
    story.append(
        p(
            "El trabajo de campo (visitas, inspecciones, jornadas BPA, logística departamental) queda a cargo de los "
            "equipos territoriales / ministerio; la plataforma se diseña para <b>recibir, validar y operar</b> esos datos.",
            st["body"],
        )
    )

    story.append(p("2. Alcance de software (completo, sin recortes)", st["h2"]))
    story.append(p("Se implementa el alcance tecnológico del documento de proyecto.", st["body"]))
    story.append(p("<b>Roles</b>", st["body"]))
    story.extend(
        bullets(
            [
                "<b>Ciudadano / Comprador</b> — acceso por correo (código/enlace), exploración, comentarios identificados, mensajes privados.",
                "<b>Productor</b> — inscripción, acreditación ministerial, vitrina digital, fotos/videos, respuesta a clientes.",
                "<b>Ministerio</b> — bandeja de altas, aprobación/rechazo/observación, moderación, fiscalización.",
            ],
            st,
        )
    )
    story.append(Spacer(1, 4))
    story.append(p("<b>Módulos</b>", st["body"]))
    story.extend(
        bullets(
            [
                "Autenticación y perfiles diferenciados (hectáreas, cultivos, volúmenes, certificaciones, tipos de venta).",
                "Red social: publicaciones, comentarios, mensajería, moderación.",
                "Geolocalización y rutas (API de mapas): pines, accesos, distancias a rutas troncales (RN 38 / RN 79) y centros urbanos.",
                "Trazabilidad y BPA digital: trabajos culturales, insumos, actas de inspección.",
                "Capacitación digital: manuales y videotutoriales.",
                "Panel ministerial: acreditación, historial, filtros por rubro y departamento.",
                "Media optimizada para 3G/4G rural + fichas compartibles (WhatsApp/redes).",
            ],
            st,
        )
    )
    story.append(Spacer(1, 4))
    story.append(p("<b>Entrega soberana</b>", st["body"]))
    story.extend(
        bullets(
            [
                "Código fuente completo (backend, frontend, apps móviles, esquemas de BD).",
                "Despliegue inicial en infraestructura bajo control del Estado.",
                "Credenciales raíz, llaves y dominios oficiales.",
                "Documentación técnica y guías de mantenimiento evolutivo.",
            ],
            st,
        )
    )

    story.append(p("3. Fuera de alcance de esta cotización", st["h2"]))
    story.extend(
        bullets(
            [
                "Despliegue territorial en 18 departamentos.",
                "Visitas a fincas, agrimensura e inspecciones oculares.",
                "Talleres BPA presenciales y convenios municipales.",
                "Mantenimiento post Mes 9 (cotizable aparte).",
                "Costos de infraestructura/licencias del Estado (Maps, storage, servidores).",
            ],
            st,
        )
    )

    story.append(p("4. Mejoras que proponemos (sobre el pliego)", st["h2"]))
    story.append(
        p(
            "Cumplimos el pliego y, además, proponemos soluciones que elevan la operación real en campo y la "
            "sostenibilidad para el Estado. Priorización de común acuerdo en Mes 1, sin desplazar obligaciones del pliego.",
            st["body"],
        )
    )
    story.append(
        make_table(
            ["Mejora", "Por qué importa"],
            [
                ["Núcleo unificado web + móvil (PWA + app)", "Menos fragmentación y menor costo evolutivo para la Provincia"],
                ["Modo offline / campo", "Útil con señal intermitente en zonas rurales"],
                ["Tablero de indicadores ministeriales", "Visibilidad de adopción, altas y cobertura por departamento"],
                ["Asistente IA para fichas productivas", "Acelera la carga de perfiles en jornadas de inscripción"],
                ["Alertas de vencimientos / documentación", "Apoyo a control de certificaciones y exigencias documentales"],
                ["Audit log de cambios", "Quién modificó qué dato y cuándo"],
                ["Búsqueda avanzada reforzada", "Departamento + rubro + geo-radio + modalidad de venta"],
            ],
            [7.5 * cm, 9 * cm],
        )
    )

    story.append(p("5. Stack tecnológico propuesto", st["h2"]))
    story.append(
        make_table(
            ["Capa", "Tecnología (propuesta)"],
            [
                ["Web", "Next.js (React) + PWA"],
                ["Móvil", "App nativa multiplataforma (React Native / Expo) sobre el mismo backend"],
                ["API / Backend", "Node.js (o runtime equivalente) + API REST/JSON"],
                ["Base de datos", "PostgreSQL"],
                ["Auth", "Roles diferenciados + acceso ciudadano por magic link / OTP email"],
                ["Media", "Storage + pipeline de compresión de imágenes/video"],
                ["Mapas", "Google Maps Platform (u API equivalente definida con la Provincia)"],
                ["Hosting", "Despliegue soberano en infraestructura provincial"],
                ["Repos", "Entrega completa de código fuente al cierre"],
            ],
            [4.5 * cm, 12 * cm],
        )
    )
    story.append(p("Stack definitivo se valida en la mesa de arquitectura del Mes 1.", st["small"]))

    story.append(p("6. Inteligencia artificial en el desarrollo", st["h2"]))
    story.append(
        p(
            "Para un software de 9 meses con alta exigencia institucional, Metis Studio desarrolla con los "
            "<b>mejores modelos disponibles</b> para cada tarea —priorizando Anthropic de última generación y "
            "complementando con herramientas especializadas cuando aporten valor:",
            st["body"],
        )
    )
    story.append(
        make_table(
            ["Modelo / capacidad", "Uso en este proyecto"],
            [
                ["Claude Opus 5.5", "Arquitectura, lógica compleja, revisiones profundas"],
                ["Fable 5", "Implementación sostenida en ciclos largos"],
                ["Claude Sonnet (última gen.)", "Desarrollo diario de módulos e iteración rápida"],
                ["Claude Haiku / ligeros", "Tareas de volumen: chequeos, borradores, clasificación"],
                ["Modelos con visión", "Apoyo en fotos de producción y validaciones visuales"],
                ["Embeddings / búsqueda semántica", "Buscador y descubrimiento de productores más preciso"],
            ],
            [6 * cm, 10.5 * cm],
        )
    )
    story.append(Spacer(1, 6))
    story.append(
        p(
            "<b>Incluido en la metodología:</b> arquitectura, implementación, pruebas, detección de edge cases y "
            "documentación continua. <b>En el producto:</b> asistentes IA (p. ej. ayuda a fichas) como mejora propuesta priorizable.",
            st["body"],
        )
    )
    story.append(
        p(
            "<b>Gobernanza del código:</b> la IA acelera el trabajo; <b>quien audita, decide y responde por lo entregado "
            "es el equipo humano de Metis Studio</b>. Los modelos están al servicio del desarrollo; la responsabilidad "
            "técnica permanece por encima del código generado.",
            st["body"],
        )
    )

    story.append(p("7. Cronograma (resumen)", st["h2"]))
    story.append(
        make_table(
            ["Mes", "Hito software"],
            [
                ["1", "Arquitectura, co-diseño, Alfa (auth/roles/perfiles/admin base)"],
                ["2", "Avance módulos + sandbox + plan marcha blanca"],
                ["3", "Marcha blanca, ajustes, Beta"],
                ["4", "Apertura de altas / circuito de acreditación en producción"],
                ["5", "Geo operativa + estadísticas parciales"],
                ["6", "Trazabilidad/BPA digital + corte de mitad de proyecto"],
                ["7", "Performance, filtros territoriales, soporte a expansión"],
                ["8", "Consolidación de datos + stress tests"],
                ["9", "Lanzamiento, entrega de código/llaves/hosting, traspaso"],
            ],
            [2 * cm, 14.5 * cm],
        )
    )
    story.append(p("Detalle completo en Anexo C.", st["small"]))

    story.append(p("8. Propuesta económica", st["h2"]))
    story.append(
        make_table(
            ["Concepto", "Monto"],
            [
                ["Honorarios mensuales de desarrollo", "USD 3.500"],
                ["Plazo", "9 meses"],
                ["Total", "USD 31.500"],
            ],
            [11 * cm, 5.5 * cm],
        )
    )
    story.append(Spacer(1, 6))
    story.extend(
        bullets(
            [
                "Facturación mensual (sin pago único).",
                "Acta de conformidad mensual sobre entregables de software.",
                "Código fuente y soberanía de datos al Mes 9.",
                "Mantenimiento posterior: cotización aparte si se requiere.",
                "El honorario cubre el <b>servicio integral</b>: dedicación del equipo, herramientas y <b>costo operativo de los modelos de IA</b> usados de forma continua durante los 9 meses.",
            ],
            st,
        )
    )

    story.append(p("9. Equipo, prioridad y disponibilidad", st["h2"]))
    story.append(p("<b>Metis Studio</b> — Matías Santana y Tomás Castiglioni.", st["body"]))
    story.append(
        p(
            "<b>Prioridad exclusiva:</b> durante estos 9 meses, RedAgro La Rioja será el <b>único</b> desarrollo de "
            "CRM / plataforma que tome Metis Studio. Es la máxima prioridad del estudio: no se reparte el equipo entre "
            "varios productos en paralelo como suele ocurrir en una software factory.",
            st["body"],
        )
    )
    story.extend(
        bullets(
            [
                "Disponibilidad en <b>horario laboral</b> para reuniones con equipos técnicos del organismo.",
                "Participación en mesas de co-diseño y marcha blanca.",
                "Comunicación directa con la contraparte (WhatsApp / canales acordados).",
                "Cumplimiento de hitos de software sujetos a dependencias del organismo.",
                "Auditoría humana de todo el código asistido por IA antes de cada entrega.",
            ],
            st,
        )
    )

    story.append(p("10. Condiciones y riesgos gestionados", st["h2"]))
    story.extend(
        bullets(
            [
                "Demoras por dependencia de la Provincia / financiador / equipos territoriales <b>no se imputan</b> al proveedor de software.",
                "El alcance territorial no forma parte de esta cotización.",
                "Año electoral: se prioriza transferencia temprana de conocimiento y documentación para sostenibilidad institucional.",
                "Posibles multas por incumplimiento aplican a hitos de software bajo control del equipo; no a operaciones de campo ajenas.",
            ],
            st,
        )
    )

    story.append(p("11. Próximos pasos", st["h2"]))
    story.extend(
        bullets(
            [
                "Revisión de esta propuesta con Cecilia / Provincia.",
                "Ajustes menores de alcance o priorización de mejoras.",
                "Demo clickeable de pantallas clave (envío en el transcurso del día).",
                "Definición contractual vía la estructura que designe la contraparte.",
                "Kickoff técnico en enero.",
            ],
            st,
        )
    )

    # ——— ANEXO A ———
    story.append(PageBreak())
    story.append(p("Anexo A — Alcance", st["annex"]))
    story.append(hr())
    story.append(p("Proveedor: Metis Studio · Duración: 9 meses · Moneda: USD", st["small"]))

    story.append(p("1. Alcance incluido (software completo según pliego)", st["h2"]))
    story.append(
        p(
            "Se desarrolla e implementa la plataforma <b>web y móvil</b> con el alcance funcional técnico definido "
            "en el documento de proyecto, sin recortar módulos.",
            st["body"],
        )
    )

    story.append(p("1.1 Estructura de usuarios y roles", st["h2"]))
    story.append(
        make_table(
            ["Rol", "Capacidades"],
            [
                [
                    "Ciudadano / Comprador",
                    "Acceso con correo (código o enlace seguro). Recorrer perfiles, ver multimedia, comentar y mensajes privados. Sin perfil público ni publicación.",
                ],
                [
                    "Productor / Emprendedor",
                    "Inscripción con datos comerciales, ubicación y rubro. Cuenta en espera hasta acreditación. Luego: vitrina, fotos, videos, respuesta a clientes.",
                ],
                [
                    "Equipo del Ministerio",
                    "Alta/baja/observación de productores, moderación, fiscalización y validación de establecimientos.",
                ],
            ],
            [4.5 * cm, 12 * cm],
        )
    )

    story.append(p("1.2 Circuito de aprobación", st["h2"]))
    story.extend(
        bullets(
            [
                "<b>Solicitud</b> — el productor se registra y carga datos productivos.",
                "<b>Revisión</b> — el Ministerio recibe la ficha; puede solicitar corrección, observar o rechazar con motivo formal.",
                "<b>Habilitación</b> — se activa la página pública y la carga de multimedia.",
            ],
            st,
        )
    )

    story.append(p("1.3 Interacción, media y panel ministerial", st["h2"]))
    story.extend(
        bullets(
            [
                "Comentarios identificados (correo validado), mensajería privada y moderación.",
                "Compresión de imágenes para 3G/4G rural; video adaptable; fichas compartibles.",
                "Bandeja de acreditación, historial de decisiones y filtros por rubro/departamento.",
            ],
            st,
        )
    )

    story.append(p("1.4 Módulos funcionales", st["h2"]))
    story.extend(
        bullets(
            [
                "<b>Autenticación y perfiles</b> — productores, agentes ministeriales, compradores con buscador geolocalizado.",
                "<b>Geolocalización y rutas</b> — pines, accesos, distancias hacia RN 38 / RN 79 y centros urbanos.",
                "<b>Trazabilidad y BPA</b> — trabajos culturales, insumos, actas/fichas de inspección cargables.",
                "<b>Capacitación digital</b> — manuales, guías y videotutoriales.",
                "<b>Documentación técnica</b> — arquitectura, BD y guías de mantenimiento evolutivo.",
            ],
            st,
        )
    )

    story.append(p("1.5 Propiedad estatal y entrega", st["h2"]))
    story.extend(
        bullets(
            [
                "Código fuente completo en repositorios oficiales, sin licencias privativas de pago anual.",
                "Hosting y despliegue inicial soberano en infraestructura provincial.",
                "Credenciales raíz, llaves y dominios oficiales.",
                "Entornos: desarrollo, sandbox/marcha blanca y producción.",
                "Pruebas de estrés ante carga masiva de productores.",
                "Manuales digitales y videotutoriales de uso (no talleres territoriales).",
            ],
            st,
        )
    )

    story.append(p("2. Fuera de alcance (territorio)", st["h2"]))
    story.extend(
        bullets(
            [
                "Despliegue territorial en 18 departamentos; visitas, agrimensura e inspecciones oculares.",
                "Convenios municipales, logística de jornadas y talleres BPA presenciales.",
                "Impresión física masiva de manuales; muestreo testigo de campo.",
                "Rendición contable ante el financiador (salvo informes técnicos de software acordados).",
            ],
            st,
        )
    )
    story.append(
        p(
            "<b>Importante:</b> la plataforma sí incluye formularios, APIs y paneles para que ministerio y equipos "
            "de campo carguen geolocalización, fichas de inspección y datos de trazabilidad.",
            st["body"],
        )
    )

    story.append(p("3. Mejoras propuestas", st["h2"]))
    story.append(
        make_table(
            ["Mejora", "Beneficio"],
            [
                ["Arquitectura unificada web + móvil", "Un núcleo de producto; menor costo evolutivo para el Estado"],
                ["Modo offline / campo", "Carga diferida con señal intermitente"],
                ["Panel de indicadores ministeriales", "Adopción, altas y cobertura por departamento"],
                ["Asistente IA para fichas", "Acelera inscripción de productores"],
                ["Alertas de vencimientos", "Apoyo a control documental / certificaciones"],
                ["Audit log", "Quién modificó qué dato y cuándo"],
                ["Búsqueda avanzada reforzada", "Departamento + rubro + geo-radio + modalidad de venta"],
            ],
            [6.5 * cm, 10 * cm],
        )
    )

    story.append(p("4. Metodología con IA", st["h2"]))
    story.append(
        p(
            "Modelos según tarea: Claude Opus 5.5, Fable 5, Claude Sonnet, Haiku/ligeros, visión y embeddings. "
            "<b>Quien audita, decide y responde por el código es el equipo de Metis Studio.</b> La IA es herramienta "
            "de aceleración; la supervisión técnica queda siempre por encima del modelo.",
            st["body"],
        )
    )

    story.append(p("5. Dependencias del organismo", st["h2"]))
    story.extend(
        bullets(
            [
                "Mesas de co-diseño (Mes 1) y feedback de marcha blanca (Meses 2–3).",
                "Infraestructura de hosting soberano y dominios.",
                "Acceso a equipos técnicos para pruebas.",
                "Carga o integración de datos de campo por responsables territoriales.",
            ],
            st,
        )
    )
    story.append(
        p(
            "Demoras atribuibles a la contraparte no se computan como incumplimiento del proveedor de software.",
            st["body"],
        )
    )

    # ——— ANEXO B ———
    story.append(PageBreak())
    story.append(p("Anexo B — Presupuesto", st["annex"]))
    story.append(hr())
    story.append(
        p(
            "Proveedor: Metis Studio · Modalidad: honorarios mensuales · Plazo: 9 meses · Moneda: USD",
            st["small"],
        )
    )

    story.append(p("1. Resumen económico", st["h2"]))
    story.append(
        make_table(
            ["Concepto", "Monto"],
            [
                ["Honorarios mensuales", "USD 3.500"],
                ["Cantidad de meses", "9"],
                ["Total del contrato de desarrollo", "USD 31.500"],
            ],
            [11 * cm, 5.5 * cm],
        )
    )
    story.append(Spacer(1, 6))
    story.append(
        p(
            "No se contempla pago único. La facturación es <b>mensual</b>, alineada a la entrega progresiva de hitos "
            "y al hecho de que el mantenimiento posterior a la entrega del código (Mes 9) no forma parte de este contrato.",
            st["body"],
        )
    )

    story.append(p("2. Qué cubre el honorario mensual", st["h2"]))
    story.extend(
        bullets(
            [
                "Desarrollo de los módulos previstos (dedicación del equipo Metis Studio).",
                "Coordinación técnica con la contraparte en horario laboral.",
                "Ajustes de mesas de trabajo / marcha blanca (dentro del alcance).",
                "Informes técnicos de avance del componente software.",
                "Infraestructura de desarrollo asistido por IA: acceso sostenido a modelos de última generación (Anthropic y los que mejor resuelvan cada tarea), con costo operativo real a lo largo de los 9 meses.",
            ],
            st,
        )
    )
    story.append(
        p(
            "El honorario mensual financia el <b>conjunto del servicio</b>: tiempo del equipo, herramientas, modelos "
            "de IA, ambiente de desarrollo, documentación y calidad. No es un monto aislado: una parte sustancial se "
            "destina a sostener ese stack de desarrollo de alto rendimiento durante todo el proyecto.",
            st["body"],
        )
    )

    story.append(p("3. Desglose conceptual (referencia)", st["h2"]))
    story.append(
        make_table(
            ["Bloque", "Meses", "Foco"],
            [
                ["Núcleo y arquitectura", "1", "Auth/roles, arquitectura web+móvil, co-diseño, alfa"],
                ["Marcha blanca", "2–3", "Sandbox, beta, ajustes, capacitación digital a agentes"],
                ["Expansión funcional y carga", "4–8", "Geo, trazabilidad, estabilidad, altas masivas"],
                ["Cierre y transferencia", "9", "Stress tests, código, llaves, hosting, lanzamiento"],
            ],
            [5 * cm, 2.5 * cm, 9 * cm],
        )
    )
    story.append(p("El desglose es orientativo; el precio contratado es el honorario mensual fijo.", st["small"]))

    story.append(p("4. Incluido / no incluido", st["h2"]))
    story.append(p("<b>Incluido</b>", st["body"]))
    story.extend(
        bullets(
            [
                "Alcance software completo según pliego.",
                "Entrega de código fuente y despliegue inicial soberano.",
                "Manuales digitales y videotutoriales de uso.",
                "Mejoras propuestas priorizadas de común acuerdo dentro del cronograma.",
                "Costos operativos de herramientas y modelos de IA del proceso de desarrollo.",
            ],
            st,
        )
    )
    story.append(p("<b>No incluido (cotizable aparte)</b>", st["body"]))
    story.extend(
        bullets(
            [
                "Despliegue territorial, visitas, inspecciones y talleres BPA presenciales.",
                "Costos de infraestructura cloud/servidores del Estado.",
                "Mantenimiento evolutivo y soporte post Mes 9.",
                "Features adicionales fuera del pliego y de las mejoras acordadas.",
            ],
            st,
        )
    )

    story.append(p("5. Condiciones comerciales sugeridas", st["h2"]))
    story.extend(
        bullets(
            [
                "Facturación mensual por USD 3.500 (inicio o cierre de mes, a definir en contrato).",
                "Acta de conformidad técnica mensual sobre entregables de software.",
                "Inicio estimado: enero (sujeto a contratación / financiamiento).",
                "Demoras por dependencia del organismo no imputables a Metis Studio.",
                "Mantenimiento post-entrega: propuesta económica separada si la Provincia lo requiere.",
            ],
            st,
        )
    )

    story.append(p("6. Comparación de valor", st["h2"]))
    story.extend(
        bullets(
            [
                "Precio competitivo frente a consultoras de mayor estructura.",
                "Alcance sin recortar el componente software del pliego.",
                "Modelo mensual que reduce riesgo para la contraparte.",
                "Transferencia total del código al Estado al Mes 9.",
                "<b>Prioridad exclusiva:</b> durante los 9 meses, RedAgro será el único desarrollo de CRM / plataforma de Metis Studio. No se diluye en una cartera de software factory.",
            ],
            st,
        )
    )

    # ——— ANEXO C ———
    story.append(PageBreak())
    story.append(p("Anexo C — Cronograma / Gantt", st["annex"]))
    story.append(hr())
    story.append(
        p(
            "Duración: 9 meses · Proveedor: Metis Studio. Los hitos territoriales del pliego quedan a cargo de "
            "equipos de campo / ministerio. Aquí: entregables de software.",
            st["small"],
        )
    )

    story.append(p("Vista por mes (resumen de trabajo)", st["h2"]))
    story.append(
        make_table(
            ["Trabajo", "Meses"],
            [
                ["Co-diseño y arquitectura", "1"],
                ["Auth, roles, panel ministerio base", "1–2"],
                ["Perfiles productor + buscador", "1–3"],
                ["Red social (posts, comentarios, DM)", "2–4"],
                ["Media (fotos/videos, compresión)", "2–4"],
                ["Geolocalización y rutas (Maps)", "2–5"],
                ["Trazabilidad / BPA digital", "3–6"],
                ["Repositorio de capacitación digital", "3–4"],
                ["Sandbox + marcha blanca + ajustes", "2–3"],
                ["Soporte a altas masivas / APIs campo", "4–8"],
                ["Indicadores / mejoras acordadas", "5–7"],
                ["Stress test y hardening", "6–8"],
                ["Entrega código, llaves, hosting + lanzamiento", "9"],
            ],
            [11 * cm, 5.5 * cm],
        )
    )

    story.append(p("Entregables mensuales", st["h2"]))

    months = [
        (
            "Mes 1 — Inicio, arquitectura y co-diseño",
            "Puesta en marcha formal del componente software.",
            [
                "Informe técnico de arquitectura (web + app móvil).",
                "Actas / minutas de mesas de co-diseño.",
                "Versión Alfa inicial: autenticación por roles, perfiles y panel admin.",
                "Backlog priorizado del núcleo funcional.",
            ],
        ),
        (
            "Mes 2 — Avance de desarrollo y plan piloto",
            "Cierre de primera versión funcional ampliada (Alfa+) y plan de marcha blanca.",
            [
                "Reporte de módulos: perfiles, buscador, geolocalización inicial, registro de insumos (base).",
                "Plan técnico de marcha blanca y selección de usuarios piloto / agentes.",
                "Entorno sandbox desplegado.",
            ],
        ),
        (
            "Mes 3 — Marcha blanca, ajustes y capacitación temprana (digital)",
            "Validación en entorno real y beta lista para despliegue masivo.",
            [
                "Informe de marcha blanca (errores, correcciones, optimización).",
                "Material de capacitación digital para agentes ministeriales.",
                "Versión Beta lista para apertura de altas.",
            ],
        ),
        (
            "Mes 4 — Apertura de inscripciones (soporte de plataforma)",
            "Plataforma habilitada para primeras altas de productores.",
            [
                "Circuito completo solicitud → revisión → habilitación.",
                "Panel de acreditación operativo.",
                "Reporte de primeras altas en el sistema.",
                "Convenios municipales y jornadas BPA: fuera de alcance software.",
            ],
        ),
        (
            "Mes 5 — Geolocalización integrada y estadísticas",
            "Mapa operativo y primeras fichas geo vinculadas a perfiles.",
            [
                "Módulo de geolocalización/rutas estable.",
                "Estadísticas parciales de perfiles.",
                "Formularios digitales de ficha de campo para equipos territoriales.",
            ],
        ),
        (
            "Mes 6 — Mitad de ejecución y auditoría de datos (sistema)",
            "Corte técnico a 6 meses.",
            [
                "Módulo de trazabilidad/BPA con historial e actas digitales.",
                "Herramientas de contraste declaración vs. inspección.",
                "Reporte de uso del panel por agentes capacitados.",
                "Certificación física en finca: fuera de alcance software.",
            ],
        ),
        (
            "Mes 7 — Expansión departamental (capacidad de plataforma)",
            "Plataforma preparada para cobertura del interior.",
            [
                "Mejoras de performance y filtros territoriales.",
                "Actualización de matriz de accesos/distancias en sistema.",
                "Reporte de avance de inscripciones.",
            ],
        ),
        (
            "Mes 8 — Consolidación y pruebas de carga",
            "Pre-lanzamiento.",
            [
                "Consolidación de base provincial en plataforma.",
                "Informe de pruebas de estrés / estabilidad.",
                "Hardening de seguridad y checklist pre-lanzamiento.",
            ],
        ),
        (
            "Mes 9 — Cierre, lanzamiento y transferencia",
            "Entrega definitiva del software al Estado.",
            [
                "Informe técnico final del componente software.",
                "Documentación de lanzamiento oficial.",
                "Acta de traspaso: repositorios, llaves, hosting soberano, superadmin.",
                "Manuales de arquitectura, BD y mantenimiento evolutivo.",
                "Propuesta opcional de mantenimiento post-contrato (aparte).",
            ],
        ),
    ]

    for title, hito, items in months:
        block = [p(title, st["h2"]), p(f"<b>Hito:</b> {hito}", st["body"])]
        block.extend(bullets(items, st))
        story.append(KeepTogether(block))

    story.append(p("Dependencias críticas", st["h2"]))
    story.append(
        make_table(
            ["Dependencia", "Impacta"],
            [
                ["Mesas de co-diseño Mes 1", "Arquitectura y alfa"],
                ["Feedback marcha blanca Mes 2–3", "Beta"],
                ["Infraestructura / dominio provincial", "Despliegues"],
                ["Carga de datos de campo por terceros", "Geo y auditoría Mes 4–8"],
                ["Disponibilidad horaria laboral", "Todos los meses"],
            ],
            [9 * cm, 7.5 * cm],
        )
    )
    story.append(Spacer(1, 8))
    story.append(
        p(
            "Demoras de contraparte desplazan hitos sin penalizar al proveedor de software.",
            st["body"],
        )
    )
    story.append(Spacer(1, 16))
    story.append(thin_hr())
    story.append(p("Metis Studio · Propuesta RedAgro La Rioja — Solo software · Noviembre 2026", st["footer"]))

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=2 * cm,
        title="Propuesta Metis Studio — RedAgro La Rioja",
        author="Metis Studio",
    )
    doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(OUT)


if __name__ == "__main__":
    build()
