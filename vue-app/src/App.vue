<script setup>
import Header from './components/Header.vue'
import Main from './components/Main.vue'
</script>

<template>
    <header class="site-header">
        <Header/>
    </header>

        <main role="main" class="container mt-8">
            <div class="row">
                <Main/>
            </div>
        </main>
</template>


<style scoped>
header {
    line-height: 1.5;
}

.logo {
    display: block;
    margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
    header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
        margin: 0 2rem 0 0;
    }

    header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }
}

/* From django css */
body {
    background: #fafafa;
    color: #333333;
}

main {
    padding-top: 60px;
    /* Height of navbar */
}

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #444444;
}

ul {
    margin: 0;
}

.bg-steel {
    background-color: #5f788a;
}

.site-header .navbar-nav .nav-link {
    color: #cbd5db;
}

.site-header .navbar-nav .nav-link:hover {
    color: #ffffff;
}

.site-header .navbar-nav .nav-link.active {
    font-weight: 500;
}

.content-block {
    background: #ffffff;
    padding: 10px 20px;
    border: 1px solid #dddddd;
    border-radius: 3px;
    margin-bottom: 20px;
}

.article-title {
    color: #444444;
}

a.article-title:hover {
    color: #428bca;
    text-decoration: none;
}

.article-content {
    white-space: pre-line;
}

.article-img {
    height: 65px;
    width: 65px;
    margin-right: 16px;
}

.article-metadata {
    padding-bottom: 1px;
    margin-bottom: 4px;
    border-bottom: 1px solid #e3e3e3
}

.article-metadata a:hover {
    color: #333;
    text-decoration: none;
}

.article-svg {
    width: 25px;
    height: 25px;
    vertical-align: middle;
}

.account-img {
    height: 125px;
    width: 125px;
    margin-right: 20px;
    margin-bottom: 16px;
}

.account-heading {
    font-size: 2.5rem;
}

div.dataTables_filter,
div.dataTables_length {
    margin-bottom: 10px;
}
</style>
