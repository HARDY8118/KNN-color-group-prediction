<script>
  import { Color, Group } from "../lib/protos/colors_pb";
  import { GrouperClient } from "../lib/protos/colors_grpc_web_pb";

  const grouperClient = new GrouperClient("http://0.0.0.0:8081");

  let hex = "";
  let guess = "";

  function query() {
    const request = new Color();
    request.setHex(color);

    grouperClient.guess(request, {}, (err, res) => {
      if (err) {
        if (err.code == 2) {
          window.alert("Failed to connect to server");
        } else {
          console.error(err);
        }
      } else {
        guess = res.array[0];
      }
    });
  }
</script>

<main>
  <section>
    <label for="color" style="background-color: {hex || '#fff'}"
      >PICK COLOR</label
    ><br />
    <input type="color" name="color" id="color" bind:value={hex} />
    <button on:click={query}>Find {hex}</button>
  </section>
  <section>
    <div>{guess || "Select a color"}</div>
  </section>
</main>

<style>
  main {
    display: flex;
    flex-direction: row;
  }
  section {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  input#color {
    display: none;
  }

  label {
    height: 4em;
    margin: 1em;
    border: solid 1px black;
    display: flex;
    text-align: center;
  }

  button{
    margin: 1em;
    cursor: pointer;
  }

  div {
    font-size: 2em;
    margin: 1em;
  }
</style>
