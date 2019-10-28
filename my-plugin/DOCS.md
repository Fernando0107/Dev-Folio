Write your plugin documentation here.

The following parameters are used to configuration the plugin's behavior:

* **url** - The URL to POST the webhook to.

The following is a sample my-plugin configuration in your 
.drone.yml file:

```yaml
notify:
  my-plugin:
    image: Fernando0107/my-plugin
    url: http://mockbin.org/
```
