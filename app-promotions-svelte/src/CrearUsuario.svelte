<script lang="ts">
  let nombre = "";
  let dni = "";
  let foto: File | null = null;
  let mensaje = "";
  
  function handleFotoChange(event: Event) {
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      foto = input.files[0];
    }
  }

  async function crearUsuario() {
    const formData = new FormData();
    formData.append("nombre", nombre);
    formData.append("dni", dni);
    if (foto) {
      formData.append("foto", foto);
    }

    try {
      const res = await fetch("http://localhost:8000/api/usuarios", {
        method: "POST",
        body: formData
      });
      const result = await res.json();
      mensaje = result.mensaje || "✅ Usuario creado con éxito";
    } catch (err) {
      mensaje = "❌ Error al crear usuario: " + err.message;
    }
  }
</script>

<style>
.form-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

/* Estilo adaptable para pantallas más pequeñas */
input, button {
  display: block;
  margin: 10px auto;
  width: 90%; /* O incluso algo menor como 80%, según tu preferencia */
  max-width: 300px; /* Esto asegura que nunca se pase de ese ancho */
  padding: 8px;
  box-sizing: border-box;
}
</style>

<div class="form-container">
  <h2>👤 Crear Usuario</h2>
  <input type="text" bind:value={nombre} placeholder="Nombre" required />
  <input type="text" bind:value={dni} placeholder="DNI" required />
  <input type="file" accept="image/*" on:change={handleFotoChange} />

  {#if foto}
    <img src={URL.createObjectURL(foto)} alt="Vista previa" class="preview" />
  {/if}

  <button on:click={crearUsuario}>Registrar</button>
  <p>{mensaje}</p>
</div>