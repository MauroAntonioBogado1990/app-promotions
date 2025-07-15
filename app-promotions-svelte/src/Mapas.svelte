<script lang="ts">
  import { onMount } from 'svelte';
  import maplibregl from 'maplibre-gl';

  let mapContainer: HTMLDivElement;
  let latitude = -34.61;
  let longitude = -58.38;

  onMount(() => {
    // Obtener geolocalización del usuario
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        latitude = pos.coords.latitude;
        longitude = pos.coords.longitude;
        loadMap();
      },
      (err) => {
        console.error("No se pudo obtener ubicación:", err);
        loadMap(); // carga con coords por defecto
      }
    );
  });

  function loadMap() {
    const map = new maplibregl.Map({
      container: mapContainer,
      style: 'https://api.maptiler.com/maps/streets/style.json?key=', // ← tu apikey
      center: [longitude, latitude],
      zoom: 13
    });

    new maplibregl.Marker()
      .setLngLat([longitude, latitude])
      .setPopup(new maplibregl.Popup().setText("Tu ubicación"))
      .addTo(map);
  }
</script>

<style>
  .map-container {
    width: 100%;
    height: 500px;
    border: 1px solid #ccc;
  }
</style>

<h2>🗺️ Sección de visualización de mapas</h2>
<div bind:this={mapContainer} class="map-container"></div>