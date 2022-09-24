<script>
export default {
    // component options
    // declare some reactive state here.
}
</script>

<template>
    <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
            <a class="navbar-brand mr-4" href="">Perspectiv</a>
            <!-- TODO: Make Perspectiv larger-->
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle"
                aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggle">
                <div class="navbar-nav mr-auto">
                    <a class="nav-item nav-link" href="">Home</a>
                </div>
                <!-- Navbar Right Side -->
                <!-- TODO: Alight right-->
                <div class="navbar-nav">
                    <a class="nav-item nav-link" href="">Connect Accounts</a>
                    <a class="nav-item nav-link" href="">Logout</a>
                    <a class="nav-item nav-link" href="">Login</a>
                    <a class="nav-item nav-link" href="">Register</a>
                </div>
            </div>
        </div>
    </nav>
</template>