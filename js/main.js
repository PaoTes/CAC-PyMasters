const app = new Vue({
    
    el: "#app",
    data: {
        personajes: [],
        siguiente: "",
        anterior: ""
    },
    created() {
        this.fetchData('https://rickandmortyapi.com/api/character/')
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.personajes = data.results;
                    this.siguiente = data.info.next;
                    this.anterior = url;
                })
                .catch(err => {
                    console.error(err);
                })
        },
        siguiente1() {

            fetch(this.siguiente)
                .then(response => response.json())
                .then(data => {
                    this.personajes = data.results;
                    this.siguiente = data.info.next;
                    this.anterior = data.info.prev;
                })
                .catch(err => {
                    console.error(err);
                })
        
        },
        anterior1() {
            fetch(this.anterior)
                .then(response => response.json())
                .then(data => {
                    this.personajes = data.results;
                    this.siguiente = data.info.next;
                    this.anterior = data.info.prev;
                })
                .catch(err => {
                    console.error(err);
                })
        }
    }
});