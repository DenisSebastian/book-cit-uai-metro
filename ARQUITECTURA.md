# Arquitectura editorial del libro digital

## Alcance

El libro desarrolla solo la sesión 6, **Anticipación y prevención**, del curso *Seguridad comunitaria y territorio* para funcionarios de análisis de Metro 2026. El prefacio presenta las ocho sesiones del curso sin identificar a sus otros docentes; destaca con color la sesión 6 y cierra con los datos de su profesor, Denis Berroeta González. Sus encabezados son breves para facilitar la lectura; las descripciones conservan el sentido del syllabus.

## Navegación

| Página | Tiempo docente | Función |
|---|---:|---|
| `index.qmd` · Prefacio | — | Sitúa la sesión dentro del curso completo. |
| `06-anticipacion-prevencion.qmd` · Introducción | 10 min | Presenta la pregunta, la agenda y un ejemplo documentado. |
| `06a-enfoques-preventivos.qmd` · Enfoques de prevención | 40 min | Presenta cada enfoque en una subsección, los relaciona en un diagrama y aplica sus diferencias a acoso, hurtos y comercio no autorizado en Metro. |
| `06b-datos-territoriales.qmd` · Datos de seguridad | 40 min | Explica la importancia de los registros; distingue fuentes externas e internas de Metro y su vinculación espacial; interpreta el contexto con la MBHT, el SII y un ejemplo de variables del diagnóstico de Las Condes. |
| Pausa | 15 min | |
| `06c-lectura-espacial.qmd` · Análisis espacial | 40 min | Explora patrones, concentraciones, hotspots, exposición y vulnerabilidades; vuelve del foco a una hipótesis situacional verificable. |
| `06d-modelamiento.qmd` · Modelamiento espacial | 40 min | Define resultado, variables y escala; introduce regresión y dependencia espacial; lee el caso de Las Condes y delimita qué aporta al análisis de Metro sin atribuir causalidad. |
| `conclusiones.qmd` · Conclusiones | 10 min | Página final independiente: cierra el circuito entre análisis y enfoques, coordinación territorial y seguimiento. |

La clase se realiza de **14:30 a 17:45**. La introducción, los cuatro bloques de 40 minutos y la página final de conclusiones suman **180 minutos lectivos**, más una pausa de 15 minutos. Las conclusiones quedan fuera de los cuatro bloques temáticos y aparecen como capítulo sin numeración en la navegación. Es una sesión panorámica: los casos y métodos se leen como referencias, sin actividades ni elaboración de una ficha de decisión durante la clase.

## Caso y criterio editorial

El hilo conductor es la **secuencia metodológica**: problema, mecanismo preventivo, datos, patrón espacial, modelamiento y decisión revisable. El anuncio de seguridad y operación de Metro para marzo de 2025 es **un ejemplo documentado entre otros**, citado con autor institucional y año. La introducción distingue, como inferencia analítica, anticipación operativa ante el retorno de marzo y medidas anunciadas para prevención o respuesta, sin atribuirles efectos medidos. La nota lleva el título «Autoridades presentan plan marzo seguro en Metro», mientras su texto se refiere al Plan de Seguridad Operacional; el libro no usa el título periodístico como nombre formal del plan. El material distingue hechos publicados, preguntas docentes y decisiones que necesitarían registros internos. El documento base `../Contenidos_modulo_anticipacion_prevencion_METRO_2026.md` utilizaba el caso ficticio «Estaciones A y B»; el libro no inventa cifras por estación.

El recorrido pasa de la ciudad a la red, las estaciones, los accesos y sus entornos. ENUSC, CEAD, STOP e IDE Chile aparecen donde corresponde como fuentes de contexto o análisis; registros operacionales y observación permitirían estudiar escalas más finas. El bloque de datos presenta la MBHT del CIT-UAI con sus dimensiones de accesibilidad, socioeconómica, ambiental y seguridad; las estadísticas comunales del SII se tratan como contexto económico y no como localización de establecimientos ni medición directa de población flotante. La introducción muestra un esquema de Metro que incluye la Línea 3 y trazados de proyectos, con un enlace al plano operativo de Red Movilidad. El libro utiliza tablas, **cinco imágenes vectoriales de diagramas**: un flujo por bloque y una comparación de los tres enfoques. Las versiones estáticas del libro conservan la paleta Archify y usan rótulos ampliados; el texto explicativo va en los pies de figura y en el capítulo. Las especificaciones JSON y los HTML interactivos están en `diagramas/`, junto al generador `svg_legibles.py`. El bloque de prevención añade un esquema docente de teorías de criminalidad; el bloque de datos incorpora una captura del portal STOP de Carabineros para el entorno de Tobalaba. Los bloques de análisis y modelamiento añaden siete imágenes docentes en `images/`: la lámina de Tobler en análisis espacial, la de Lefebvre en modelamiento, tres pasos de KDE y dos láminas del estudio CIT-UAI de Las Condes. La página independiente de conclusiones incorpora una ilustración conceptual de coordinación territorial. El texto distingue la captura STOP de un diagnóstico vigente de Metro, la demostración KDE de una estadística oficial, la fecha 2017 impresa en las láminas del estudio presentado en 2018 y la imagen de coordinación de una reunión real.

La revisión de 2026 añadió fuentes primarias y casos de aplicación: el estudio territorial de la Subsecretaría de Prevención del Delito con datos CEAD y sectores CIT-UAI, estadísticas de transporte de Londres y estudios metodológicos publicados por UNODC, NIJ y el Center for Problem-Oriented Policing. Cada aplicación a Metro distingue hechos públicos de hipótesis docentes.

El bloque de datos trata la Ley 21.659 y su reglamento. La ley no establece entrega automática de datos del CEAD para estudios de seguridad; la aplicación de deberes específicos de una entidad obligada requiere verificar la resolución correspondiente. También se anota el cambio previsto de régimen de datos personales el 1 de diciembre de 2026.

## Fuentes base

- `../Syllabus Curso Seguridad Comunitaria y Territorio_2026_METRO.pdf`: objetivo y contenidos de la sesión 6, además del contexto del curso.
- `../Contenidos_modulo_anticipacion_prevencion_METRO_2026.md`: secuencia, conceptos y actividades originales.
- [Gobierno de Santiago, «Autoridades presentan plan marzo seguro en Metro» (2025)](https://www.gobiernosantiago.cl/2025/02/27/autoridades-presentan-plan-marzo-seguro-en-metro/): anuncio de medidas de seguridad y operación.
