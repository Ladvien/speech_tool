:py:mod:`speech_neuron.kokoro_server`
=====================================

.. py:module:: speech_neuron.kokoro_server

.. autodoc2-docstring:: speech_neuron.kokoro_server
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SpeechNeuronServer <speech_neuron.kokoro_server.SpeechNeuronServer>`
     - .. autodoc2-docstring:: speech_neuron.kokoro_server.SpeechNeuronServer
          :summary:

API
~~~

.. py:class:: SpeechNeuronServer(config: speech_neuron.config.NodeConfig)
   :canonical: speech_neuron.kokoro_server.SpeechNeuronServer

   .. autodoc2-docstring:: speech_neuron.kokoro_server.SpeechNeuronServer

   .. rubric:: Initialization

   .. autodoc2-docstring:: speech_neuron.kokoro_server.SpeechNeuronServer.__init__

   .. py:method:: generate_speech(text: str, voice: str = None, speed: typing.Union[float, int] = None, split_pattern: str = None)
      :canonical: speech_neuron.kokoro_server.SpeechNeuronServer.generate_speech

      .. autodoc2-docstring:: speech_neuron.kokoro_server.SpeechNeuronServer.generate_speech

   .. py:method:: stream_file(stream: typing.Any)
      :canonical: speech_neuron.kokoro_server.SpeechNeuronServer.stream_file
      :async:

      .. autodoc2-docstring:: speech_neuron.kokoro_server.SpeechNeuronServer.stream_file
