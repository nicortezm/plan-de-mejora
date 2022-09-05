<template>

    <br><br><br><br>
    <div class="container-lg">
        <SaveComponent :key="manga" :mangaEdit="manga" @mangaInsert="mangaInsert" @mangaUpdate="mangaUpdate" />
        <div class="table-responsive">
            <div class="table-wrapper">
                <div class="table-title">
                    <div class="row">
                        <div class="col-sm-4">
                            <h2>Detalle <b>Mangas</b></h2>
                        </div>

                    </div>
                </div>
                <table class="table table-bordered">
                    <thead>
                        <tr>
                            <th>#</th>
                            <th>Nombre</th>
                            <th>Autor</th>
                            <th>Volumenes</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>

                        <tr v-for="(m, index) in mangas" :key="m._id.$oid">
                            <td>{{ index }}</td>
                            <td>{{ m.nombre }}</td>
                            <td>{{ m.autor }}</td>
                            <td>{{ m.volumenes }}</td>
                            <td>
                                <button @click="mangaEdit(m, index)">Editar</button>
                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>
        </div>
    </div>
    <br><br><br><br>



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