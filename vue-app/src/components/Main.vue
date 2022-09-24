<script>
import InvestmentsGrid from "./InvestmentsGrid.vue";
export default {
    data() {
        return {
            username: "John Doe",
            user_email: "john.doe@gmail.com",
            total_valuation: 1000000,
            last_update: "2021-01-01",
        };
    },
    components: { InvestmentsGrid }
}
</script>

<template>
    <div class="content-section mt-4">
        <div class="row content-block">
            <div class="col-4">
                <!-- Move to navbar right with an icon (and remove either username or email)-->
                <h3>{{ username }}</h3>
                <p class="text-secondary">{{ user_email}}</p>
            </div>
            <div class="col-4 text-center">
                <div class="row">
                    <h2 style="color:#5f788a">{{ total_valuation }}€</h2>
                </div>
                <div class="row">
                    <h6 style="color:#5f788a">TOTAL VALUATION</h6>
                </div>
            </div>
            <div class="col-4 text-center">
                <!-- TODO: Align righ -->
                <div class="row"><small class="text-muted"><i>{{ last_update }}</i></small></div>
                <!-- TODO: Align bottom -->
                <div class="row text"><small class="text-muted"><i>Last Update</i></small></div>

            </div>
        </div>
        <div class="row content-block">
            <h4>Investments</h4>
            <div class="container">
                <InvestmentsGrid />
            </div>
        </div>
    </div>
</template>