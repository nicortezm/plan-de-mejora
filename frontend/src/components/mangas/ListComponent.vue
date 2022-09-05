<template>
    <h1> Listado de Mangas</h1>

    <SaveComponent :key="manga" :mangaEdit="manga" @mangaInsert="mangaInsert" @mangaUpdate="mangaUpdate" />

    <div v-for="(m, index) in mangas" :key="m._id.$oid">
        <button @click="mangaEdit(m, index)">Editar</button>
        {{ m.nombre }}

    </div>
    <!-- <button @click="manga = ''">Crear</button> -->

</template>

<script>

import SaveComponent from "./SaveComponent.vue";
export default {
    components: { SaveComponent },
    data() {
        return {
            mangas: [],
            manga: "",
            mangaIndex: 0,
        };
    },
    methods: {
        mangaInsert: function (manga) {
            console.log("Insertar Manga")
            this.mangas.push(manga)
        },
        mangaEdit: function (manga, index) {
            this.mangaIndex = index
            this.manga = manga
            console.log("Editar")
        },
        mangaUpdate: function (manga) {
            this.mangas[this.mangaIndex].nombre = manga.nombre
        }
    },
    mounted() {
        fetch("http://127.0.0.1:5000/mangas")
            .then((res) => res.json())
            .then((res) => this.mangas = res);
    },
}

</script>