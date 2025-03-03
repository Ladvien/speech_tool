:py:mod:`speech_tool.kokoro_server`
===================================

.. py:module:: speech_tool.kokoro_server

.. autodoc2-docstring:: speech_tool.kokoro_server
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`SpeechToolServer <speech_tool.kokoro_server.SpeechToolServer>`
     - .. autodoc2-docstring:: speech_tool.kokoro_server.SpeechToolServer
          :summary:

API
~~~

.. py:class:: SpeechToolServer(config: speech_tool.config.NodeConfig)
   :canonical: speech_tool.kokoro_server.SpeechToolServer

   .. autodoc2-docstring:: speech_tool.kokoro_server.SpeechToolServer

   .. rubric:: Initialization

   .. autodoc2-docstring:: speech_tool.kokoro_server.SpeechToolServer.__init__

   .. py:method:: generate_speech(text: str, voice: str = None, speed: typing.Union[float, int] = None, split_pattern: str = None)
      :canonical: speech_tool.kokoro_server.SpeechToolServer.generate_speech

      .. autodoc2-docstring:: speech_tool.kokoro_server.SpeechToolServer.generate_speech

   .. py:method:: stream_file(stream: typing.Any)
      :canonical: speech_tool.kokoro_server.SpeechToolServer.stream_file
      :async:

      .. autodoc2-docstring:: speech_tool.kokoro_server.SpeechToolServer.stream_file
