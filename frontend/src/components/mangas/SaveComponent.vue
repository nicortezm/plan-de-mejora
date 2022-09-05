<template>
    <h1> Registrar Mangas</h1>

    <form @submit="sendForm">
        <label for="">Nombre Manga</label>
        <input type="text" v-model="manga.nombre">
        <br>
        <label for="">Nombre Autor</label>
        <input type="text" v-model="manga.autor">
        <br>
        <label for="">Cantidad volumenes</label>
        <input type="number" v-model="manga.volumenes">

        <input type="submit" value="Enviar">
    </form>
</template>

<script>

export default {
    props: ['mangaEdit'],
    emits: ["mangaInsert", "mangaUpdate"],
    data() {
        return {
            manga: {
                nombre: "",
                autor: "",
                volumenes: ""
            }
        }
    },
    methods: {
        sendForm() {
            // e.preventDefault();
            const formData = new FormData();
            formData.append('autor', this.manga.autor);
            formData.append('nombre', this.manga.nombre);
            formData.append('volumenes', this.manga.volumenes);
            if (this.mangaEdit == "") {
                this.insert(formData)
            } else {
                this.update(formData)
            }
        },
        insert(formData) {
            fetch("http://127.0.0.1:5000/mangas", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(Object.fromEntries(formData))
            }).then((res) => res.json())
                .then((manga) => this.$emit("mangaInsert", manga))
        },
        update(formData) {

            fetch("http://127.0.0.1:5000/mangas/" + this.mangaEdit._id.$oid, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(Object.fromEntries(formData))
            }).then((res) => res.json())
                .then((manga) => this.$emit("mangaUpdate", manga))
        }
    },
    mounted() {
        if (this.mangaEdit != "") {
            this.manga.nombre = this.mangaEdit.nombre
            this.manga.autor = this.mangaEdit.autor
            this.manga.volumenes = this.mangaEdit.volumenes
        }
    }

}

</script>