const synth = new Tone.Synth({
    volume: -15, // -15dB
    oscillator: {
      type: 'triangle' // triangle wave 
    },
    envelope: {
      attack: 0.03, // 30ms attack
      release: 1 // 1s release
    }
}).toMaster()


AFRAME.registerComponent('synth', {
   // dependencies: ['raycaster'],  // for oculus go laser controls
    schema: {
        // Describe the property of the component.
        note: {
            // NOTE: type: 'string' is referring to our Aframe component's property type, not a synth preset
            type: 'string', 
            default: 'C4' // C4 default note
          },
        duration: {
            type: 'string',
            default: '4n' // quarter note default time
          }
    },
  
    init: function () {
      // Do something when component first attached.
      // this.el.addEventListener('raycaster-intersection', this.trigger.bind(this)) // for oculus go laser controls
      this.el.addEventListener('fusing', this.trigger.bind(this))
    },
  
    trigger: function () {
      synth.triggerAttackRelease(this.data.note, this.data.duration)
    },
  
    remove: function () {
      // Do something the component or its entity is detached.
    },
  
    tick: function (time, timeDelta) {
      // Do something on every scene tick or frame.
    }
});