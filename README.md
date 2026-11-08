# VICENSÆ

**Always Give and Keep Your Dreams Alive.**

Public repository for VICENSÆ design, typography, provenance and public-service protocol documentation.

## Instalación rápida · 3 pasos

**1. Descarga el proyecto.** En GitHub pulsa **Code → Download ZIP**, descomprime el archivo y abre la carpeta `design/v1.0/`. Si usas Git:

```bash
git clone https://github.com/PeopleArtFactory/VICENSAE.git
cd VICENSAE/design/v1.0
```

**2. Prueba el diseño sin instalar nada.** Abre `preview/index.html` con tu navegador. Verás los colores, la tipografía de respaldo, las pastillas y una demostración de voz mediante el navegador. La voz no es todavía la voz oficial VICENSÆ.

**3. Instálalo en PAF4 (SvelteKit).** Copia `src/tokens.css` y `src/components.css` a `src/lib/styles/VICENSAE/v1.0/` dentro de tu aplicación. Después importa los estilos en tu `src/routes/+layout.svelte`:

```svelte
<script lang="ts">
  import '$lib/styles/VICENSAE/v1.0/components.css';
</script>
```

Aplica la clase `vaes` al contenedor principal de la interfaz. No hace falta instalar paquetes npm para usar estos estilos.

> **Importante:** este paquete **no instala una fuente VICENSÆ propia**: todavía no existen en el repositorio archivos `.woff2`, `.ttf` ni `.otf` verificados. Inter y Raleway son referencias tipográficas; para incorporarlas debes obtener sus archivos y licencias de los proyectos originales.

Más detalles: [guía de instalación SvelteKit](design/v1.0/install/INSTALL_SVELTEKIT.md) · [vista previa](design/v1.0/preview/index.html) · [manual de diseño](design/v1.0/docs/DESIGN_MANUAL.md).

## Design Handbook v1.0

The `design/v1.0/` directory contains design tokens, CSS components, a browser preview, SvelteKit integration and provenance templates. This initial release does **not** contain installable VICENSÆ font binaries or a proprietary voice model.

**Typography provenance:** Inter and Raleway are upstream references, generally licensed under SIL OFL 1.1. Their actual binaries and any derived font files must retain applicable upstream license requirements, copyrights and Reserved Font Name restrictions. Do not relicense OFL derivatives under PSL.

**PSL/VPPL:** the canonical legal text and nomenclature must be verified before asserting any new component is licensed under those terms.

**Happy Egress† by Design:** open formats, exportability and verifiable origins. Demo is not a verified fiduciary admission.

QR-FR+ · PUBLIC DESIGN HANDBOOK v1.0 · PROVENANCE PENDING
