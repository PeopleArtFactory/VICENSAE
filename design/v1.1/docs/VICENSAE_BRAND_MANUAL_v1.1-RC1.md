# VICENSÆ — Manual de marca y sistema de diseño v1.1 RC1

**Estado:** CANDIDATO DE DISEÑO · NO APROBADO COMO MARCA MAESTRA · SIN ADMISIÓN FIDUCIARIA.  
**Fecha:** 2026-11-09. **Repositorio destino:** PeopleArtFactory/VICENSAE.  
**Principio:** **Always Happy Egress† by Design.**

## 1. Propósito y personalidad
VICENSÆ es una identidad para experiencias que deben ser claras, accesibles, auditables y exportables. La marca combina precisión técnica, hospitalidad cultural y dignidad institucional. El diseño nunca reemplaza una prueba ni confiere derechos. La libertad es una consecuencia en sí misma; no es un dato mutable.

**Atributos:** claridad, continuidad, apertura, sobriedad, humanidad, precisión, permanencia y respeto a la autoría.  
**Voz:** directa, técnica cuando procede, no grandilocuente al describir garantías; distinción explícita entre hipótesis, demo, verificación local y admisión real.

## 2. Arquitectura de marca
- **VICENSÆ:** identidad paraguas; en código, rutas, paquetes y archivos usar `VICENSAE` ASCII.
- **PAF4:** creación y galerías; conservar su identidad y el verde PAF sujeto a contraste y verificación del máster.
- **QSONG Æ:** obra, revelación y audioguía; experiencia obsidiana y oro.
- **VÆS:** expresión institucional/cultural, a concretar.
- **COIIRM hub:** aplicación institucional; respetar marca y permisos propios del Colegio.
- **Fiduciary Computation:** documentación científica con tratamiento editorial, sin trasladar una estética de producto a afirmaciones científicas.

## 3. Nombre, logotipo y símbolo
**Denominación visible:** `VICENSÆ` (Æ U+00C6); **denominación técnica:** `VICENSAE`. No sustituir automáticamente una por otra en nombres de archivo o API.  
**Wordmark provisional:** composición tipográfica «VICENSÆ»; **no constituye el logo maestro**. El logotipo final requiere archivo vectorial maestro, áreas de protección, tamaños mínimos y variantes aprobadas.  
**Símbolo:** Æ es una ligadura identitaria, no un certificado criptográfico. La geometría ortogonal/fractal es una línea de exploración, no un activo registrado. No crear falsas marcas de conformidad ni sellos oficiales.

**Usos correctos:** contraste suficiente; proporciones originales; espacio libre; versiones monocromas accesibles; alt text.  
**Usos prohibidos:** deformar el símbolo, reemplazar glifos de forma ambigua en identificadores, emplear iconografía de verificación sin resultado real, usar el logo del COIIRM sin autorización, llamar «oficial» a un prototipo.

## 4. Color
### Paleta principal — candidato
- Obsidiana `#090A0F`: fondo oscuro.
- Azul nocturno `#07121C`: variante institucional.
- Grafito `#1B1B22`: superficies.
- Oro `#EAC878`: acento principal.
- Marfil `#F7F3E8`: texto en oscuro.
- Gris `#A7A7B2`: texto secundario.

### Semántica
- Éxito `#97E5B7`; advertencia `#FFD27D`; error `#FFB6AE`; información `#A7C8FF` **en tema oscuro**. Las equivalencias claras se definen en `tokens/semantic.json`. Los estados requieren texto e iconografía además del color.
- Verde PAF candidato `#2EB88A`: **no aprobado** como valor maestro; verificar referencia gráfica original.

**Regla:** el oro identifica acciones o jerarquía, nunca certifica legitimidad. Prohibido usar «verde» como único indicador de admisión.

## 5. Tipografía
**Estrategia:** una identidad original inspirada en la claridad de Inter, elegancia de Raleway y precisión industrial de IBM Plex; las fuentes definitivas **no existen aún**. Hasta disponer de binarios licenciados, utilizar stacks con fallback local.

| Nivel | Uso | Stack provisional |
| --- | --- | --- |
| UI | navegación, lectura, formularios | Inter / IBM Plex Sans / system-ui |
| Display | titulares, portadas | Raleway / Inter |
| Mono | hashes, estados, tiempos, cifras tabulares | IBM Plex Mono / monospace |
| Canon | manifiestos, textos constitucionales | IBM Plex Serif / Georgia |

La familia propia requerirá contornos originales, métricas, kerning, diacríticos españoles, cifras tabulares, pruebas a 12–18 px, WOFF2/TTF/OTF y procedencia de fuentes. No atribuir una fuente inexistente a VICENSÆ ni relicenciar derivados OFL bajo PSL.

## 6. Retícula, espaciado y forma
Unidad base de **4 px**; escala 4/8/12/16/20/24/32/40/48 px. Controles interactivos de al menos **44 px**. Radios 8/12/18/24 px; pastillas 999 px. Ancho editorial recomendado 1200 px, con columnas fluidas y adaptación móvil. El diseño debe tolerar zoom 200%, textos largos y cinco idiomas canónicos cuando se definan.

## 7. Componentes
**Fundamentales:** Shell, Header, Sidebar, Navigation, Button, Link, Input, Select, Checkbox, Switch, Card, Modal, Tooltip, Tabs, Toast, Notice, Badge, DataField, Table, EmptyState, LoadingState.  
**Fiduciarios:** VerificationPanel, EvidenceDigest, CustodyReceipt, WitnessPresence, AdmissionStatus, ProfileDisclosure, ExportReceipt, EventTimeline.  
**Culturales:** ArtworkViewport, RevealLayer, RevealedText, AudioGuide, EarthTimeMeter, CreditsLedger, ExportBundle.

Todos los componentes requieren estados `default`, `hover`, `focus-visible`, `disabled`, `loading`, `error`, `success`, `empty`, `offline` donde proceda. Las implementaciones de UI no emiten ni modifican actos fiduciarios.

## 8. Gramática de estados fiduciarios
| Estado | Mensaje permitido |
| --- | --- |
| DRAFT | «Borrador. No constituido.» |
| LOCAL_VERIFIED | «Integridad local coincidente; no acredita autoridad.» |
| DEGRADED_VALIDATION | «Verificación parcial; faltan evidencias.» |
| FULL_FOR_PROFILE | «Suficiente para el perfil indicado, según verificador autenticado.» |
| MISMATCH | «Discrepancia detectada.» |
| INVALID_STRUCTURE | «Estructura inválida.» |
| UNSUPPORTED_PROFILE | «Perfil no soportado.» |
| WITHHOLD | «Admisión suspendida.» |

**Nunca** mostrar «VERIFIED IMMUTABLE ARTIFACT», «MAINNET ACTIVE» o un bloque génesis inventado como resultado real. El estado debe venir de un servicio verificador autorizado y acompañado por perfil, evidencia y alcance. Una comparación SHA-256 local no demuestra firma, autoría, legitimidad o continuidad histórica.

## 9. Patrones de producto
**QSONG:** la lámina puede desplazarse y ampliarse; el texto revelado se lee y copia; la audioguía aparece después del texto; velocidad configurable; los segundos de escucha se miden por tiempo monotónico terrestre. El servidor autoriza cualquier cobro. No entregar píxeles protegidos al navegador antes de la autorización: CSS no es criptografía.

**PAF4:** preservar retrocompatibilidad, metadatos y exportación de obras; evitar duplicar los componentes comunes.  
**COIIRM hub:** distinguir acreditación histórica, estado actual y revocación legítima; no presentar la verificación de un QR como garantía jurídica universal.  
**VICENSÆ / DFD:** testigos, custodios, verificación, admisión y ejecución tienen roles diferentes; no se confunden mediante color o lenguaje visual.

## 10. Accesibilidad y contenido
Objetivo de diseño: WCAG 2.2 AA, **pendiente de auditoría**. Navegación completa por teclado, `:focus-visible`, anuncios ARIA no intrusivos, etiquetas explícitas, contraste probado, zoom, movimiento reducido, no autoplay, equivalentes textuales y exportaciones legibles. Nunca depender exclusivamente del color, del audio o de una animación para transmitir una decisión.

## 11. Movimiento, voz e imagen
Transiciones funcionales 120–200 ms, desactivables; evitar animaciones de éxito que sugieran admisión. La voz sintética del navegador es demo, no «voz oficial VICENSÆ». Toda obra y voz deben llevar atribución, alcance de derechos y procedencia. La estética cinematográfica es un recurso expresivo, no una licencia para usar material ajeno.

## 12. Licencias y procedencia
El repositorio v1.0 declara que los binarios tipográficos y la voz oficial no están publicados. Verificar licencias de cada fuente exacta, hash, commit, avisos y restricciones de nombres reservados. **PSL/VPPL permanece pendiente de texto jurídico canónico**. No declarar dominio público a materiales sin autorización verificable. No incluir claves privadas, audios de terceros ni pruebas simuladas en distribuciones públicas.

## 13. Publicación, gobernanza y control de cambios
Fuente única: `tokens/core.json` + `tokens/semantic.json`; CSS generado y revisado. Versionado SemVer y changelog. Los adaptadores SvelteKit, React y HTML consumen las mismas definiciones. Congelar `design/v1.0` y publicar candidatos en ramas/PR. Revisión humana para identidad gráfica, licencias, accesibilidad y estados fiduciarios antes de pasar a producción.

**Criterios de aceptación:** preview offline, tema claro/oscuro, estados sin falsa admisión, controles ≥44 px, tests de tokens y contraste, fuentes con licencias verificadas, exportaciones abiertas, pruebas responsive y aprobación del máster visual.

## 14. Pendientes de decisión
1. Logo maestro vectorial, versión fractal/ortogonal y reglas de marca.
2. Familia tipográfica original y alcance de derivados OFL.
3. Valor oficial del verde PAF y variantes institucionales.
4. Texto jurídico canónico PSL/VPPL y derechos de los activos.
5. Voz VICENSÆ, cinco idiomas y licencias de locución.
6. Componentes de producción con adaptadores autenticados a verificador, custodia y cobro.
7. Auditoría WCAG 2.2 AA, seguridad y rendimiento.

---

**QR-FR+ · BRAND & DESIGN CANDIDATE v1.1 RC1 · PRODUCTION WITHHOLD**
