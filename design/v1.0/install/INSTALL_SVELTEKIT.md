# Integración SvelteKit / PAF4

Copiar `src/tokens.css` y `src/components.css` a `src/lib/styles/VICENSAE/v1.0/`. En el layout global importar:

```svelte
<script lang="ts">
  import '$lib/styles/VICENSAE/v1.0/components.css';
</script>
<slot />
```

Usar `class="vaes"` en el contenedor. Con snippets de Svelte 5, reemplazar slot por `{@render children()}` en su layout correspondiente.

Los binarios de fuentes no se incluyen. Obtener versiones precisas desde upstream, conservar avisos OFL y servirlas localmente si se desea. Evitar dependencias de CDN para aplicaciones de custodia offline.
